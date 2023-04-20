import numpy as np
seed=42
np.random.seed(seed)
from matplotlib import pyplot as plt
from skimage.filters import threshold_mean
from skimage.transform import resize

def reshape(data):
    """Reshape flattened 1D array to 2D image

    :param data: flattened image array
    :type data: np.ndarray of shape (n,)
    :return: data
    :rtype: np.ndarray of shape (sqrt(n), sqrt(n))
    """
    dim = int(np.sqrt(len(data)))
    data = np.reshape(data, (dim, dim))
    return data

def get_corrupted_input(input, corruption_level):
    """Get image with noise added
    
    :param input: image array to be corrupted
    :type input: np.ndarray
    :param corruption_level: corruption level, range [0.0-1.0]
    :type corruption_level: np.float
    :return: corrupted image
    :rtype: np.ndarray
    """
    corrupted = np.copy(input)
    inv = np.random.binomial(n=1, p=corruption_level, size=len(input))
    for i, v in enumerate(input):
        if inv[i]:
            corrupted[i] = -1 * v
    return corrupted

def plot(data, test, predicted, figsize=(3, 3), savefig=False):
    """Plot training images, corrupted inputs and predictions side by side
    
    :param data: training images; atleast 3
    :type data: list of np.ndarray with len >=3
    :param test: corrupted (test) versions of training images; atleast 3
    :type test: list of np.ndarray with len >=3
    :param predicted: predictions for images in test; atleast 3
    :type predicted: list of np.ndarray with len >=3
    :param figsize: size for matplotlib figure; defaults to (3, 3)
    :type figsize: tuple
    :param savefig: boolean value to save matplotlib figure; defaults to False
    :type savefig: bool
    :return: None
    """
    data = [reshape(d) for d in data]
    test = [reshape(d) for d in test]
    predicted = [reshape(d) for d in predicted]
    
    fig, axarr = plt.subplots(len(data), 3, figsize=figsize)
    for i in range(len(test)):
        if i==0:
            axarr[i, 0].set_title('Training Image')
            axarr[i, 1].set_title("Noisy Input Image")
            axarr[i, 2].set_title('Prediction')
            
        axarr[i, 0].imshow(data[i])
        axarr[i, 0].axis('off')
        axarr[i, 1].imshow(test[i])
        axarr[i, 1].axis('off')
        axarr[i, 2].imshow(predicted[i])
        axarr[i, 2].axis('off')
            
    plt.tight_layout()
    if savefig:
        plt.savefig("result.png")
    plt.show()

def preprocessing(img):
    """Perform thresholding to convert grayscale image to binary and return flattened

    :param img: grayscale image array
    :type data: np.ndarray of shape (n, n)
    :return: flatten
    :rtype: np.ndarray of shape (n^2,)
    """
    w, h = img.shape
    thresh = threshold_mean(img)
    binary = img > thresh
    shift = 2*(binary*1)-1
    flatten = np.reshape(shift, (w*h))
    return flatten