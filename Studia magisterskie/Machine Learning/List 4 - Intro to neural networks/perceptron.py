"""Perceptron Implementation."""

import numpy as np


class Perceptron:
    """Single-Layer Perceptron Classifier."""

    def __init__(self, n_inputs: int, learning_rate: float = 0.1, random_state: int = None):
        """
        Initialize a Perceptron.

        Parameters:
        -----------
        n_inputs : int
            Number of input features
        learning_rate : float
            Learning rate (eta) for weight updates
        random_state : int or None
            Random seed for reproducibility
        """
        self.n_inputs = n_inputs
        self.learning_rate = learning_rate
        self.random_state = random_state
        self._initialize_weights()

    def _initialize_weights(self):
        """Initialize weights and bias to small random values."""
        rng = np.random.RandomState(self.random_state)
        self.weights = rng.normal(loc=0.0, scale=0.01, size=self.n_inputs)
        self.bias = 0.0

    def activation(self, z: np.ndarray) -> np.ndarray:
        """
        Step activation function.

        Returns:
        --------
        int: 1 if z >= 0, else 0 (or -1 for bipolar version)
        """
        return np.where(z >= 0, 1, 0)

    def forward(self, X: np.ndarray) -> np.ndarray:
        """
        Compute perceptron output.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_inputs)
            Input features

        Returns:
        --------
        array-like, shape (n_samples,)
            Predictions (0 or 1)
        """
        X = np.atleast_2d(X)
        z = np.dot(X, self.weights) + self.bias
        return self.activation(z)

    def fit(self, X: np.ndarray, y: np.ndarray, n_epochs: int = 100) -> "Perceptron":
        """
        Train the perceptron using the perceptron learning algorithm.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_inputs)
            Training features
        y : array-like, shape (n_samples,)
            Target values (0 or 1)
        n_epochs : int
            Maximum number of training epochs

        Returns:
        --------
        self : Perceptron
            Fitted perceptron

        Note: Store training history in self.errors_ (errors per epoch)
        """
        X = np.array(X)
        y = np.array(y)
        self.errors_ = []
        self.weight_history_ = [{"weights": self.weights.copy(), "bias": self.bias}]
        for _epoch in range(n_epochs):
            errors = 0
            for xi, target in zip(X, y, strict=True):
                prediction = self.forward(xi.reshape(1, -1))[0]
                error = target - prediction

                self.weights += self.learning_rate * error * xi
                self.bias += self.learning_rate * error

                errors += int(error != 0)

            self.errors_.append(errors)
            self.weight_history_.append({"weights": self.weights.copy(), "bias": self.bias})
            if errors == 0:
                break

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_inputs)
            Input features

        Returns:
        --------
        array-like, shape (n_samples,)
            Predicted class labels
        """
        return self.forward(X)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Compute classification accuracy.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_inputs)
            Input features
        y : array-like, shape (n_samples,)
            True labels

        Returns:
        --------
        float
            Accuracy score (0 to 1)
        """
        predictions = self.predict(X)
        return np.mean(predictions == y)
