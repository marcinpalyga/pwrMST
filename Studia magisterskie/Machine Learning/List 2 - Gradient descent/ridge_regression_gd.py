import numpy as np


class RidgeRegressionGD:
    """
    Ridge Regression using Gradient Descent.
    """
    
    def __init__(self, alpha=1.0, learning_rate=0.01, num_iterations=1000, 
                verbose=True):
        """
        Initialize the Ridge Regression model.
        """
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.verbose = verbose
        self.theta = None
        self.loss_history = []
    
    def _compute_loss(self, X, y, theta):
        """
        Compute MSE loss with L2 regularization.
        """
        m = len(y)
        predictions = X @ theta
        mse_loss = (1/(2*m)) * np.sum((predictions - y)**2)
        reg_term = (self.alpha/(2*m)) * np.sum(theta[1:]**2)
        total_loss = mse_loss + reg_term
        return total_loss
    
    def _compute_gradient(self, X, y, theta):
        """
        Compute gradient with L2 regularization.
        """
        m = len(y)
        predictions = X @ theta
        gradient = (1/m) * X.T @ (predictions - y)
        reg_term = np.zeros_like(theta)
        reg_term[1:] = (self.alpha/m) * theta[1:]
        gradient += reg_term
        return gradient
    
    def fit(self, X, y):
        """
        Fit the ridge regression model using gradient descent.
        """
        prev_loss = 10**6
        X_b = np.hstack([np.ones((X.shape[0],1)), X])
        self.theta = np.zeros(X.shape[1]+1)
        for i in range(self.num_iterations):
            gradient = self._compute_gradient(X_b, y, self.theta)
            self.theta = self.theta - self.learning_rate*gradient
            loss = self._compute_loss(X_b, y, self.theta)
            self.loss_history.append(loss)
            if i%100 == 0 and self.verbose == True:
                print(f'Iteration: {i}, loss:{loss}')
        return self
    
    
    def predict(self, X):
        """
        Make predictions on new data.
        """
        X_b = np.hstack([np.ones((X.shape[0], 1)), X])
        return X_b @ self.theta

