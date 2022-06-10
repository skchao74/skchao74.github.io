def update_w_j(rho, t_x_over_J, inverse_XXT, X_j, y_j, w_bar):
    """
    :param rho: tuning param rho
    :param t_x_over_J: t_x/J
    :param inverse_XXT: inverse of (rho I - X_j X_j^T)
    :param X_j: jth row of matrix X
    :param y_j: jth row of matrix y from kth iteration
    :param w_bar: w_bar from kth iteration
    :return: w_j for the (k+1)th iteration
    """
    if type(X_j) != np.ndarray or len(X_j) == 1:
        raise ValueError("invalid X_j: {}, {}".format(type(X_j), X_j))
    next_w_j = np.dot(inverse_XXT, X_j - t_x_over_J - y_j + rho * w_bar)
    return project_w(next_w_j, X_j)

def project_w(w_j: np.ndarray, X_j: np.ndarray) -> np.ndarray:
    """
    if X_j^T w_j + 1 < 0, then project w_j to hyperplane (X_j^T w_j + 1 = 0)
    """
    dot_product = np.dot(X_j, w_j) + 1 
    if dot_product >= 0:
        return w_j
    else:
        return w_j - (dot_product / np.sum(X_j ** 2)) * X_j

def matrix_inverse(rho: float, X_j: np.array, method: str = "sherman_morrison") -> np.ndarray:
    """
    :param X_j: one row of matrix X
    :return: inverse of (rho I - X_j X_j^T)
    (rho I - X_j X_j^T) ^ -1 = rho^-1 I + X_j X_j^T / (rho^2 - rho ||X_j||^2)
    """
    if len(X_j) == 1:
        raise ValueError("X_j = {} has length of 1, please check.".format(X_j))
    if method == "sherman_morrison":
        denominator = rho * rho - rho * np.sum(X_j ** 2)
        numerator = np.matmul(X_j.reshape(-1, 1), X_j.reshape(1, -1))
        return 1 / rho * np.identity(len(X_j)) + numerator / denominator
    elif method == "numpy":
        return np.linalg.inv(rho * np.identity(len(X_j)) - \
                np.matmul(X_j.reshape(-1, 1), X_j.reshape(1, -1)))
    else:
        raise ValueError("method is not supported, only support 'sherman_morrison' or 'numpy'")
    return
	
class MicroSynth(object):
    """
    MicroSynth docstring
    """
    def __init__(self, index, args: dict):
        self.iterations = args["iterations"]
        self.rho = args["rho"]
        self.output_dataset = args["output_dataset"]
        input_dataset = args["input_dataset"]
        input_table_prefix = args["input_table_prefix"]
        self.mu = args.get("mu", 5)
        self.tau1 = args.get("tau1", 2)
        self.tau2 = args.get("tau2", 2)

        self.input_table = f'sc-dig.{input_dataset}.{input_table_prefix}{index}'
        self.output_tb_suffix = f'iter{self.iterations}_mu_{self.mu}_rho_{str(self.rho).replace(".", "")}_{input_table_prefix}{index}'

        # declare attributes here
        self.J = None # control total count
        self.num_features = None # number of features
        self.t_x_over_J = None # sum of treatment group divided by J
        self.t_x = None # avg of treatment group
        self.c_df = None
        self.t_df = None
        self.result = None

    def process_input_table(self, spark_session): # spark_session: read data from bigquery

        df = read_big_query_table(spark_session, self.input_table)
        df.cache()

        feature_col_names = [col_name for col_name in df.columns if col_name not in ['ghost_user_id', 'treated_group']]
        feature_cols = [f.col(col_name) for col_name in feature_col_names]
        self.num_features = len(feature_cols)

        self.c_df = get_control_df(df, feature_cols, True)
        self.c_df.cache()
        self.J = self.c_df.count()
        print("J = ", self.J)

        self.t_df = get_t_df(df, feature_cols, feature_col_names)
        self.t_df.cache()

        treatment_count = df.filter("treated_group = 1").count()
        self.t_x = np.array(self.t_df.collect()[0].avg_x) # mean of treatment group
        self.t_x_over_J = self.t_x * treatment_count / self.J # what's the use of it?

    def pre_calculate_inverse_matrices(self):
        """
        calculate inverse of matrices, for each row of
        c_df, we pre-calculate the inverse of (rho I - X_j X_j^T)
        """
        rho, num_features = self.rho, self.num_features
        # rdd has schema of (x, inverse_matrix, w, y)
        self.c_rdd = self.c_df.rdd.map(
            lambda p: (np.array(p.x), 
                    matrix_inverse(rho, np.array(p.x), method="sherman_morrison"),
                    np.zeros(num_features),
                    np.zeros(num_features)
                    )
        )
        self.w_bar = np.zeros(self.num_features)
        self.c_rdd.persist(StorageLevel.MEMORY_AND_DISK)


    def calculate_w_bar(self, rdd):
        w_bar = rdd.reduce(
            lambda x, y: [0, 0, x[2] + y[2]]
        )
        return w_bar[2] / self.J

    def one_iteration(self) -> None: # main iteration
        """
        this function takes self.c_df as input and compute the next iteration
        """
        rho, t_x_over_J, w_bar = self.rho, self.t_x_over_J, self.w_bar
        next_w_rdd = self.c_rdd.map(
            lambda p: (
                p[0], 
                p[1], 
                update_w_j(rho, t_x_over_J, p[1], p[0], p[3], w_bar),
                p[3]
            )
        )
        w_bar = self.calculate_w_bar(next_w_rdd)
        self.c_rdd = next_w_rdd.map(
            lambda p: (
                p[0],
                p[1],
                p[2],
                p[3] + rho * (p[2] - w_bar)
            )
        )
        self.prev_w_bar, self.w_bar = self.w_bar, w_bar
        self.c_rdd.persist(StorageLevel.MEMORY_AND_DISK)
        next_w_rdd.unpersist()
        return


    def calculate_c_x(self): # for balance check?
        """
        weight for user j is 1 + \\xi_j ^ T X_j
        """
        res = self.c_rdd.map(lambda p: ((1 + np.dot(p[0], p[2])),
                                     (1 + np.dot(p[0], p[2])) * np.array(p[0]))
        ).reduce(
            lambda a, b: (a[0] + b[0], a[1] + b[1])
        )
        return res[1] / res[0]

    def calculate_residual(self):
        w_bar = self.w_bar
        R = self.c_rdd.map(lambda p: np.sum((p[2] - w_bar) ** 2)).reduce(lambda x, y: x + y)
        self.R = np.sqrt(R)
        self.S = self.rho * np.sqrt(self.J * np.sum((self.w_bar - self.prev_w_bar) ** 2))
        print(self.R, self.S)
        if self.R > self.S * self.mu:
            self.rho *= self.tau1
        elif self.R < self.S / self.mu:
            self.rho /= self.tau2


    def solve(self): # main loop?
        self.pre_calculate_inverse_matrices()
        control_means = list()
        diff = list()
        for i in range(self.iterations):
            print("iteration: ", i, "rho: ", self.rho)
            self.one_iteration()
            c_x = self.calculate_c_x()
            control_means.append((i, c_x.tolist()))
            diff.append((i, np.subtract(c_x, self.t_x).tolist(), (np.subtract(c_x, self.t_x) / self.t_x).tolist()))

            # check condition
            self.calculate_residual()

        self.result = [control_means, diff]