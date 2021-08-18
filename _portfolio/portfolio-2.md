---
title: "Statistical inference within distributed or cloud data ecosystem"
excerpt: "My goal is to develop methods that can be smoothly implemented in the ecosystem of data science, and perform provabiy accurate statistical analysis including hypothesis testing on statistical models and causal effect.<br/><img src='/images/research/distributed.png' style='width: 40%; height: auto'>"
collection: portfolio
---
According to the <a href="https://online.hbs.edu/blog/post/data-ecosystem" target="_blank"> Harvard Business School Online</a>, the term data ecosystem refers to the programming languages, packages, algorithms, cloud-computing services, and general infrastructure an organization uses to collect, store, analyze, and leverage data. The data ecosystem has become increasingly complex in order to efficiently analyze excessively large datasets that arise with the business activities and the advance of technology. Challenges arise when one wants to perform sophisticated statistical analysis within a complex data ecosystem.

The price of operating in a complex data ecosystem, where data are usually stroed in cloud or in distributed computing system, is positively associated with the number of passes over the entire dataset of interest. Unfortunately, popular numerical routines usually require many passes. For example, one gradient descent iteration typically requires one pass over the entire dataset, and fitting a logistic regression can take hundreds or thousands of iterations. In addition, in data science practice, one often needs multiple querries over the entire dataset in order to perform a certain task. Passes over entire data is not only costly but also inefficient as computational overhead may occur. Hence, minimizing the number of queries without sacrificing statistical accuracy is most desirable in practice. 

My research goal is thus to develpe provable methods that can be performed with one or just a few passes over the entire dataset while maintaining oracle inferential accuracy such as size and power. Our main theoretical output, the minimal number of passes $\tau_{\min}$ over entire dataset, often depend on the type of models, e.g. linear or logistic regression model, complexity (dimensionality) and the computational power. Our methods can be used to perform inference for regression models, e.g. linear, logistic regression or even quantile regression.

My vision is to create methods that can be seamlessly integrated into the daily data science applications hosted in cloud or distributed computational framework, for example using large user data with billions of entries to test the effect after a feature in an app is introduced.

<img src='/images/research/minimaltau.png' style='width: 45%; height: auto' class='center'>
<img src='/images/research/microsynth.png' style='width: 45%; height: auto' class='center'>

Research outputs and further reading
-
<li>Yang, Y., Chao, S.-K. and Cheng, G. (2021). Distributed Bootstrap for Simultaneous Inference Under High Dimensionality, arXiv: 2102.10080. [<a href="https://arxiv.org/abs/2102.10080" target="_blank">pdf</a>]
<li>Yu, Y., Chao, S.-K. and Cheng, G. (2020). Simultaneous Inference for Massive Data: Distributed Bootstrap. <em>ICML 2020</em> (acceptance rate: 21.8%). [<a href="https://icml.cc/virtual/2020/poster/6606" target="_blank">ICML paper/slides/video</a>] [<a href="https://arxiv.org/pdf/2002.08443.pdf" target="_blank">Arxiv</a>]</li>
<li>Volgushev, S., Chao, S.-K. and Cheng, G. (2019). Distributed inference for quantile regression processes. <em>Annals of Statistics</em>, 47(3): 1634-1662. [<a href="http://arxiv.org/abs/1701.06088" target="_blank">arXiv</a>] [<a href="https://projecteuclid.org/euclid.aos/1550026852" target="_blank">pdf</a>] [<a href="/files/portfolio/20190608 talk_ICSA.pdf" target="_blank">talk</a>] [<a href="/files/portfolio/SAMSI_WISO_BDQR.pdf" target="_blank">poster</a>][<a href="https://www.connectedpapers.com/main/59a68cb52566a1901268e1032df14c9328dce7c7/Distributed-inference-for-quantile-regression-processes/graph"  target="_blank">context</a>]</li>

