"""Simple Multi-Layer Perceptron (MLP) Implementation."""

import numpy as np


class SimpleMLP:
    """Simple Multi-Layer Perceptron with One Hidden Layer."""

    def __init__(
        self, n_input: int, n_hidden: int, n_output: int, learning_rate: float = 0.1, random_state: int = None
    ):
        """
        Initialize a simple MLP with one hidden layer.

        Parameters:
        -----------
        n_input : int
            Number of input features
        n_hidden : int
            Number of hidden neurons
        n_output : int
            Number of output neurons
        learning_rate : float
            Learning rate for gradient descent
        random_state : int or None
            Random seed for reproducibility
        """
        self.n_input = n_input
        self.n_hidden = n_hidden
        self.n_output = n_output
        self.learning_rate = learning_rate

        rng = np.random.RandomState(random_state)
        self.W1 = rng.randn(n_input, n_hidden) * np.sqrt(2.0 / n_input)
        self.b1 = np.zeros(n_hidden)
        self.W2 = rng.randn(n_hidden, n_output) * np.sqrt(2.0 / n_hidden)
        self.b2 = np.zeros(n_output)

        self.z1 = None
        self.a1 = None
        self.z2 = None
        self.a2 = None

    def sigmoid(self, z: np.ndarray) -> np.ndarray:
        """Sigmoid activation function."""
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

    def sigmoid_derivative(self, a: np.ndarray) -> np.ndarray:
        """
        Return derivative of sigmoid.

        Note: Input is the activation a = sigmoid(z), not z.
        Formula: a * (1 - a).
        """
        return a * (1 - a)

    def forward(self, X: np.ndarray) -> np.ndarray:
        """
        Forward pass.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_input)
            Input data

        Returns:
        --------
        output : array-like, shape (n_samples, n_output)
            Network predictions

        Note: Store intermediate values (z1, a1, z2, a2) for backprop.
        """
        X = np.atleast_2d(X)
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)

        return self.a2

    def backward(self, X: np.ndarray, y: np.ndarray) -> dict:
        """
        Backward pass (compute gradients).

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_input)
            Input data
        y : array-like, shape (n_samples, n_output)
            Target values

        Returns:
        --------
        gradients : dict
            Dictionary with 'dW1', 'db1', 'dW2', 'db2'
        """
        X = np.atleast_2d(X)
        y = np.atleast_2d(y)
        m = X.shape[0]

        delta2 = self.a2 - y
        dW2 = np.dot(self.a1.T, delta2) / m
        db2 = np.sum(delta2, axis=0) / m

        delta1 = np.dot(delta2, self.W2.T) * self.sigmoid_derivative(self.a1)
        dW1 = np.dot(X.T, delta1) / m
        db1 = np.sum(delta1, axis=0) / m

        return {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}

    def fit(self, X: np.ndarray, y: np.ndarray, n_epochs: int = 1000, verbose: bool = True) -> "SimpleMLP":
        """
        Train the network.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_input)
            Training data
        y : array-like, shape (n_samples, n_output)
            Target values
        n_epochs : int
            Number of training epochs
        verbose : bool
            Print loss every 100 epochs

        Returns:
        --------
        self : SimpleMLP
            Fitted MLP

        Note: Store loss history in self.loss_history_
        """
        X = np.array(X)
        y = np.array(y).reshape(-1, self.n_output)

        self.loss_history_ = []

        for epoch in range(n_epochs):
            y_pred = self.forward(X)
            loss = self.compute_loss(y, y_pred)
            self.loss_history_.append(loss)
            gradients = self.backward(X, y)

            self.W1 -= self.learning_rate * gradients["dW1"]
            self.b1 -= self.learning_rate * gradients["db1"]
            self.W2 -= self.learning_rate * gradients["dW2"]
            self.b2 -= self.learning_rate * gradients["db2"]

            if verbose and (epoch % 100 == 0 or epoch == n_epochs - 1):
                print(f"Epoch {epoch}/{n_epochs}, Loss: {loss:.6f}")

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions (threshold at 0.5 for binary classification)."""
        output = self.forward(X)
        return (output >= 0.5).astype(int)

    def compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Compute binary cross-entropy loss.

        Formula: -1/m * sum(y*log(y_pred) + (1-y)*log(1-y_pred))

        Note: Add small epsilon (1e-15) to prevent log(0).
        """
        epsilon = 1e-15
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        m = y_true.shape[0]
        loss = -np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)) / m
        return loss
