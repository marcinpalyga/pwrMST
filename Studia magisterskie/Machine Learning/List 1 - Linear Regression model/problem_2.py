"""Ridge Regression implementation using closed-form solution."""

import numpy as np


class RidgeRegression:
    """
    Ridge Regression with L2 regularization.
    """

    def __init__(self, alpha: float = 1.0) -> None:
        """
        Initialize Ridge Regression model.

        Args:
            alpha: Regularization parameter (λ in the book).
        """
        self.alpha = alpha
        self.theta = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "RidgeRegression":
        """
        Fit the Ridge Regression model.

        Args:
            X: Training features of shape (n_samples, n_features).
            y: Target values of shape (n_samples,).

        Returns:
            self: Returns the instance itself.
        """
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])
        n_features = X_b.shape[1]
        L = self.alpha * np.eye(n_features)
        L[0, 0] = 0

        self.theta = np.linalg.inv(X_b.T @ X_b + L) @ X_b.T @ y
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions using the fitted model.

        Args:
            X: Features of shape (n_samples, n_features).

        Returns:
            Predicted values of shape (n_samples,).
        """
        if self.theta is None:
            raise ValueError("Model has not been fitted yet.")

        X_b = np.hstack([np.ones((X.shape[0], 1)), X])
        return X_b @ self.theta
