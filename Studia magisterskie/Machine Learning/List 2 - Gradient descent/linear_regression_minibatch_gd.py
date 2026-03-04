import numpy as np


class LinearRegressionMiniBatchGD:
    """
    Linear Regression using Mini-Batch Gradient Descent.
    """
    
    def __init__(self, learning_rate=0.01, num_epochs=100, batch_size=32, verbose=False):
        """
        Initialize the Linear Regression Mini-Batch GD model.
        """
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.verbose = verbose
        self.theta = None
        self.loss_history = []
        
    def _compute_loss(self, X, y, theta):
        """Compute MSE loss"""
        m = len(y)
        predictions = X @ theta
        loss = (1/(2*m)) * np.sum((predictions - y)**2)
        return loss
    
    def _compute_gradient(self, X_batch, y_batch, theta):
        """Compute gradient of MSE loss"""
        m = len(y_batch)
        predictions = X_batch @ theta
        gradient = (1/m) * X_batch.T @ (predictions - y_batch)
        return gradient
    
    def fit(self, X, y):
        """
        Fit the linear regression model using Mini-Batch GD.
        """
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])
        self.theta = np.zeros(X.shape[1]+1)
        for epoch in range(self.num_epochs):
            indices = np.arange(X_b.shape[0])
            np.random.shuffle(indices)
            X_shuffled = X_b[indices]
            y_shuffled = y[indices]
            for i in range(0, X_b.shape[0], self.batch_size):
                end_idx = min(i + self.batch_size, X_b.shape[0])
                X_batch = X_shuffled[i:end_idx]
                y_batch = y_shuffled[i:end_idx]
                gradient = self._compute_gradient(X_batch, y_batch, self.theta)
                self.theta -= self.learning_rate * gradient
            loss = self._compute_loss(X_b, y, self.theta)
            self.loss_history.append(loss)
            if self.verbose and (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{self.num_epochs}, Loss: {loss:.4f}")
        return self
    
    def predict(self, X):
        """
        Make predictions using the fitted model.
        """
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])
        return X_b @ self.theta
