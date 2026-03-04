import numpy as np

class LinearRegressionGD:
    """Linear Regression using Batch Gradient Descent"""
    
    def __init__(self, learning_rate=0.01, num_iterations=1000, 
                 tolerance=1e-10, verbose=True):
        """
        Parameters:
        -----------
        learning_rate : float
            The learning rate (alpha) for gradient descent
        num_iterations : int
            Maximum number of iterations
        tolerance : float
            Convergence tolerance for loss change
        verbose : bool
            Whether to print progress information
        """
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.tolerance = tolerance
        self.verbose = verbose
        self.theta = None
        self.loss_history = []
    
    def _compute_loss(self, X, y, theta):
        """Compute MSE loss"""
        m = len(y)
        predictions = X @ theta
        loss = (1/(2*m)) * np.sum((predictions - y)**2)
        return loss
    
    def _compute_gradient(self, X, y, theta):
        """Compute gradient of MSE loss"""
        m = len(y)
        predictions = X @ theta
        gradient = (1/m) * X.T @ (predictions - y)
        return gradient
    
    def fit(self, X, y):
        """
        Fit the linear regression model using gradient descent
        
        Parameters:
        -----------
        X : numpy array of shape (m, d)
            Training features (without intercept column)
        y : numpy array of shape (m,)
            Training targets
            
        Returns:
        --------
        self : object
            Returns self for method chaining
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
            loss_change = np.abs(prev_loss-loss)
            if loss_change < self.tolerance:
                if self.verbose == True:
                    print(f"Converged at iteration {i}")
                break
            prev_loss = loss
        return self
    
    def predict(self, X):
        """
        Make predictions on new data
        
        Parameters:
        -----------
        X : numpy array of shape (m, d)
            Feature matrix (without intercept column)
            
        Returns:
        --------
        predictions : numpy array of shape (m,)
            Predicted target values
        """
        X_b = np.hstack([np.ones((X.shape[0],1)), X])
        return X_b@self.theta
