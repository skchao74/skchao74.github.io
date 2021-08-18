---
title: "Regularized stochastic algorithms with application to deep neural networks"
excerpt: "The goal is to develop a family of provable stochastic algorithms for e.g. large scale optimization and training deep neural networks. The provability is established by probabilistic weak approximation and the ordinary differential equation theory. <br/><img src='/images/research/intro_cifar100_conn_thumb.png' style='width: 45%; height: auto'>"
collection: portfolio
---
My goal is to develop a family of provable stochastic algorithms with regularization, that is generically applicable to many machine learning problems, such as regression, principal component analysis and deep learning. A variant of our algorithm with $\ell_1$ penalty, called directional pruning (DP), finds a solution in the same minimum valley where SGD is located on the deep learning loss landscape of CIFAR100, but with over 90% sparsity (left panel in the figure below). For large scale dataset like ImageNet, DP is competitive in the high sparsity regime relative to other methods, as shown in the right panel below where our performance is marked by red crosses.

<img src='/images/research/intro_cifar100_conn_thumb.png' style='width: 50%; height: auto;'>
<img src='/images/research/imagenet.png' style='width: 45%; height: auto;'>

The provability of our algorithm is obtained by two steps. The first is the observation that our algorithm has a mirror desent behavior as it updates a stochastic process in the dual space, and then a mirror map takes the process to the primal space. Next, after recognizing that the process in the dual space is a Markov process, we approximate it with a stochastic differential equation rigorously in the sense of weak approximation. The figure below shows the behavior of three coordinates of our algorithm with $\ell_1$ regularization. In this case the mirror map is a soft-thresholding operator corresponding to the green shaded area in the dual space. Since $v_{101}$ lies mainly in the green area, it is thresholded to 0 in the primal space. Our theory approximates the zigzaging empirical trajectories by smooth curves, which is the solution of an multivariate ordinary differential equation, and captures their random variation in the primal space by the confidence bands in blue. 

Our theory can be used to study intriguing interactions between regularization and a complex loss landscape in optimization problem like deep learning, and to obtain theoretical guarantees such generalization bound. Our method has been applied by <a href="https://arxiv.org/abs/2003.11235" target="_blank">AutoFIS</a> and <a href="https://arxiv.org/pdf/2107.05328" target="_blank">structural directional pruning</a>.

<img src='/images/research/vwplot.png' style='width: 90%; height: auto;'>

Reseach outputs and further reading
-
<li>Chao, S.-K., Wang, Z., Xing, Y. and Cheng, G. (2020). Directional Pruning of Deep Neural Networks. <em>NeurIPS 2020</em>. [<a href="https://arxiv.org/abs/2006.09358" target="_blank">pdf</a>] [<a href="/files/portfolio/NeurIPS2020_17484_slides.pdf" target="_blank">Short Slides</a>][<a href="/files/portfolio/sparse_nn_NeurIPS_poster.pdf" target="_blank">Poster</a>][<a href="https://github.com/donlan2710/gRDA-Optimizer" target="_blank">Python code</a>][<a href="https://www.connectedpapers.com/main/19ab5e06461aca46148696fd472767079d69c5c7/Directional-Pruning-of-Deep-Neural-Networks/graph" target="_blank">context</a>]</li>

<li>Chao, S.-K. and Cheng, G. (2019). A generalization of regularized dual averaging and its dynamics. [<a href="https://arxiv.org/abs/1909.10072" target="_blank">pdf</a>] [<a href="https://github.com/donlan2710/gRDA-Optimizer" target="_blank">Python code</a>][<a href="https://www.connectedpapers.com/main/ad0ba50ad5056bdeca46a433e73b719a10164df2/A-generalization-of-regularized-dual-averaging-and-its-dynamics/graph" target="_blank">context</a>]</li>
