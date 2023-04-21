import numpy as np
seed=42
np.random.seed(seed)
from matplotlib import pyplot as plt
import matplotlib.cm as cm

class HopfieldNetwork(object):
    """Implementation of a Hopfield Network using Hebb rule and synchronous pattern recovery.
    """

    def train(self, train_data):
        """Train the network using Hebbian learning rule.

        :param train_data: list of preprocessed training images
        :type train_data: list of np.ndarray 
        :return: None
        """
        num_data =  len(train_data)
        self.num_neurons = train_data[0].shape[0]

        W = np.zeros((self.num_neurons, self.num_neurons))
        rho = np.sum([np.sum(t) for t in train_data]) / (num_data*self.num_neurons)

        for i in range(num_data):
            t = train_data[i] - rho
            W += np.outer(t, t)
        
        diagW = np.diag(np.diag(W))
        W = W - diagW
        W /= num_data
        
        self.W = W 
    
    def predict(self, data, num_iter=20, threshold=0):
        """Recover stored patterns from noisy images.

        :param data: list of corrupted samples to be reconstructed
        :type data: list of np.ndarray
        :param num_iter: number of iterations to run
        :type num_iter: int, defaults to 20
        :param threshold: activation threshold for neurons
        :type threshold: float, defaults to 0
        :return: list of predictions
        :rtype: list of np.ndarray
        """
        self.num_iter = num_iter
        self.threshold = threshold
        copied_data = np.copy(data)
        preds = []
        for i in range(len(data)):
            preds.append(self.sync_update(copied_data[i]))
        return preds
    
    def sync_update(self, init_s):
        """Synchronous update

        :param init_s: initial state; the corrupted image
        :type init_s: np.ndarray
        :return: predicted state
        :rtype: np.ndarray
        """
        s = init_s
        e = self.compute_energy(s)
        
        for i in range(self.num_iter):
            s = np.sign(self.W @ s - self.threshold)
            e_new = self.compute_energy(s)
            if e == e_new:
                return s
            e = e_new
        return s
     
    def compute_energy(self, s):
        """Compute energy of given state

        :param s: state for which energy needs to be computed
        :type s: np.ndarray
        :return: energy of state s
        :rtype: float
        """
        return -0.5 * s @ self.W @ s + np.sum(s * self.threshold)

    def plot_weight_matrix(self, figsize=(5,5)):
        """Plot weights of trained network

        :param figsize: figsize for matplotlib figure, defaults to (5,5)
        :type figsize: tuple of ints
        :return: None
        """
        plt.figure(figsize=figsize)
        w_mat = plt.imshow(self.W, cmap=cm.coolwarm)
        plt.colorbar(w_mat)
        plt.title("Weights Matrix for Trained Network")
        plt.tight_layout()
        plt.show()