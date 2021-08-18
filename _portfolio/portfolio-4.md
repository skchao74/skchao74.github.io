---
title: "Brain and lung image data analysis"
excerpt: "Clinicians rely on medical imaging to make diagonosis. I develop machine learning methods that discover subtle patterns in brain fRMI and lung MRI. <br/><img src='/images/research/output19.png' style='width: 40%; height: auto'>"
collection: portfolio
---
Medical imaging is indispensable in modern medical practice and in various scientific domains, e.g. economic research. In Chat et al. (2018), I proposed expectile factor models for the <a href="https://en.wikipedia.org/wiki/Blood-oxygen-level-dependent_imaging" target ="_blank">BOLD</a> intensities of multiple subjects in order to jointly study their risk attitude toward tasks such as selecting between two risky investments. Expectile -- a descriptive statistics for the tail of distribution -- is kwown to be more sensitive to the extreme movement, and is suitable for capturing a sharp change in BOLD. I developed a nuclear norm penalized method that encourage a lower number of factors, so that we can use only the first and the second factor to make inference.    
<img src='/images/research/bold.png' style='width: 90%; height: auto'>

 An exciting future direction is to quantify the segmentaiton uncertainty on low-contrast lung MRI. Low-contrast image with large low-intensity region(s) creates a great challenge for usual segmentation algorithms, because they typically relies heavily on the signal intensities and its patterns to make inference. For example, an algorithm may be uncertain about the regions where the signal intensity is low, so there is much uncertainty in the shape/area of the organ in the low-intensity regions. I plan to use and/or propose machine learning methods to quantify the uncertainty of segmentation. Our research output is expected to promote and enhance the clinical use of lung MRI. The methods we develop can be applied to other problems beyond segmentation including MRI reconstruction from $k$-space, denoising etc.
<img src='/images/research/lungmri.png' style='width: 96%; height: auto'>


Research outputs and further reading
---
<li><strong>Chao, S.-K.</strong>, Härdle, W. and Huang, C. (2018). Multivariate Factorizable Expectile Regression with Application to fMRI Data. <em>Computational Statistics and Data Analysis</em>, 121: 1-19. [<a href="https://www.sciencedirect.com/science/article/pii/S0167947317302542" target="_blank">pdf</a>]</li>

