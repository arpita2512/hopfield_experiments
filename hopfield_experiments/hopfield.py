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

        :param train_data: list of flattened and preprocessed training samples
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
        self.num_iter = num_iter
        self.threshold = threshold
        copied_data = np.copy(data)
        predicted = []
        for i in range(len(data)):
            predicted.append(self._run(copied_data[i]))
        return predicted
    
    def _run(self, init_s):
        """Synchronous update
        """
        s = init_s
        e = self.energy(s)
        
        for i in range(self.num_iter):
            s = np.sign(self.W @ s - self.threshold)
            e_new = self.energy(s)
            if e == e_new:
                return s
            e = e_new
        return s
    
    
    def energy(self, s):
        return -0.5 * s @ self.W @ s + np.sum(s * self.threshold)

    def plot_weight_matrix(self, cmap=cm.coolwarm):
        plt.figure(figsize=(6, 5))
        w_mat = plt.imshow(self.W, cmap=cmap)
        plt.colorbar(w_mat)
        plt.title("Network Weights")
        plt.tight_layout()
        plt.show()