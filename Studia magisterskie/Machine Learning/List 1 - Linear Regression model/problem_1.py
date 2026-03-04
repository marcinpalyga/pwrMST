"""Linear Regression implementation using closed-form solution."""

import numpy as np


class LinearRegression:
    """
    Linear Regression using Ordinary Least Squares (OLS).

    Implements Equation 3.4 from "The Elements of Statistical Learning":
    θ = (X^T X)^(-1) X^T y

    Attributes:
        theta: Coefficient vector including intercept as first element.
    """

    def __init__(self) -> None:
        """Initialize Linear Regression model."""
        self.theta = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "LinearRegression":
        """
        Fit the Linear Regression model using the closed-form solution.

        Args:
            X: Training features of shape (n_samples, n_features).
            y: Target values of shape (n_samples,).

        Returns:
            self: Returns the instance itself for method chaining.
        """
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])

        self.theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions using the fitted model.

        Args:
            X: Features of shape (n_samples, n_features).

        Returns:
            Predicted values of shape (n_samples,).

        Raises:
            ValueError: If the model has not been fitted yet.
        """
        if self.theta is None:
            raise ValueError("Model has not been fitted yet.")

        X_b = np.hstack([np.ones((X.shape[0], 1)), X])
        return X_b @ self.theta
