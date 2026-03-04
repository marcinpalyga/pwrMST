import numpy as np


class LinearRegressionSGD:
    """
    Linear Regression using Stochastic Gradient Descent.
    """
    
    def __init__(self, learning_rate=0.01, num_epochs=100, verbose=False):
        """
        Initialize the Linear Regression SGD model.
        """
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.verbose = verbose
        self.theta = None
        self.loss_history = []
        
    def _compute_loss(self, X, y, theta):
        """Compute MSE loss"""
        m = len(y)
        predictions = X @ theta
        loss = (1/(2*m)) * np.sum((predictions - y)**2)
        return loss
    
    def _compute_gradient(self, x, y, theta):
        """Compute gradient of MSE loss"""
        prediction = x @ theta
        error = prediction - y
        gradient = error * x
        return gradient
    
    def fit(self, X, y):
        """
        Fit the linear regression model using gradient descent
        """
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])
        self.theta = np.zeros(X.shape[1]+1)
        for epoch in range(self.num_epochs):
            indices = np.arange(X_b.shape[0])
            np.random.shuffle(indices)
            X_shuffled = X_b[indices]
            y_shuffled = y[indices]
            for i in range(X_b.shape[0]):
                x_i = X_shuffled[i]
                y_i = y_shuffled[i]
                gradient = self._compute_gradient(x_i, y_i, self.theta)
                self.theta -= self.learning_rate * gradient
            loss = self._compute_loss(X_b, y, self.theta)
            self.loss_history.append(loss)
            if self.verbose and (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{self.num_epochs}, Loss: {loss:.4f}")
        return self
    
    def predict(self, X):
        """
        Make predictions on new data
        """
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])
        return X_b @ self.theta
