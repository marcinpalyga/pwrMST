"""Two-Layer XOR Network Implementation."""

import numpy as np


class TwoLayerXOR:
    """2-Layer Neural Network for XOR Function."""

    def __init__(self):
        """
        Initialize a 2-layer network for XOR.

        Architecture:
        - Input: 2 neurons (x1, x2)
        - Hidden: 2 neurons (h1, h2)
        - Output: 1 neuron (y)

        You must set the weights manually to solve XOR.
        """
        self.W1 = np.array(
            [
                [1, 1],
                [1, 1],
            ]
        )
        self.b1 = np.array([-1.5, -0.5])

        self.W2 = np.array(
            [
                [-1],
                [1],
            ]
        )
        self.b2 = np.array([-0.5])

    def heaviside(self, z: np.ndarray) -> np.ndarray:
        """Step activation function."""
        return np.where(z >= 0, 1, 0)

    def forward(self, X: np.ndarray) -> tuple:
        """
        Forward pass through the network.

        Parameters:
        -----------
        X : array-like, shape (n_samples, 2)
            Input features

        Returns:
        --------
        y : array-like, shape (n_samples,)
            Network output
        h : array-like, shape (n_samples, 2)
            Hidden layer activations (for analysis)
        """
        X = np.atleast_2d(X)
        z1 = np.dot(X, self.W1) + self.b1
        h = self.heaviside(z1)
        z2 = np.dot(h, self.W2) + self.b2
        y = self.heaviside(z2).flatten()

        return y, h

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions (wrapper around forward)."""
        y, _ = self.forward(X)
        return y

    def verify_xor(self) -> bool:
        """
        Verify the network correctly computes XOR.

        Returns:
        --------
        bool
            True if all XOR outputs are correct
        """
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y_true = np.array([0, 1, 1, 0])
        y_pred = self.predict(X)
        return np.array_equal(y_pred, y_true)
