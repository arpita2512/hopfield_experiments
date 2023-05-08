#########################
Implementation Details
#########################

Note: Asynchronous Hopfield implementation is done by Ruchita Mijagiri, and for Self-Organising Maps an existing implementation, 
`MiniSom <https://github.com/JustGlowing/minisom>`_, is used.

Evaluation Strategy
**********************

To circumvent the issue of spurious states and maintain uniformity of training set size, samples from only 2 distinct 
digits are present in the training set at a time. Thus, the network is initialised and trained 5 times. The same approach 
is followed for asynchronous hopfield and self-organising map.

The test partition of MNIST is used for training, consisting of 10000 grayscale images of size (28, 28). Predictions are made 
using the same images, with varying levels (0 - 100%) of noise added. 

Parameters
****************

#. Random State: 42
#. Synchronous Hopfield
    * Number of Neurons: 784
    * Threshold: 70
    * Iterations: 30
#. Self-Organising Map
    * Size of X dim: 28
    * Size of Y dim: 28
    * Size of Input: 784
#. Asynchronous Hopfield+
    * Number of Neurons: 784
    * Threshold: 70
    * Iterations: 30

+Iterations were reduced for Asynchronous approach due to computational limitations. Since Asynchronous approach only 
updates a single neuron at a time, it takes longer to converge, as compared to Synchronous approach. Therefore, metrics for
Asynchronous approach deteriorate much more rapidly as noise increases. However, performance can improve with increased
iterations (~100000).

Metrics Used
*******************
#. Mean squared error (MSE): Average squared difference between the predicted values and the actual value; Lower is better and for perfect reconstruction MSE is 0
#. Peak signal-to-noise ratio (PSNR): Th ratio between the maximum possible pixel value and the power of noise (given by MSE), expressed using logarithmic scale; Higher is better and for perfect reconstruction PSNR is infinite
#. Structural similarity (SSIM): A weighted combination of luminance, contrast and structure in range [0, 1]; Higher is better and for perfect reconstruction SSIM is 1