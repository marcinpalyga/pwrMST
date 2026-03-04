"""
Cross-validation module.
"""

import numpy as np


class KFoldCV:
    """
    K-Fold cross-validator.
    """

    def __init__(self, n_splits: int = 5, shuffle: bool = True, random_state: int = None):
        """
        Initialize K-Fold cross-validator.

        Parameters:
        -----------
        n_splits : int
            Number of folds (default: 5)
        shuffle : bool
            Whether to shuffle data before splitting (default: True)
        random_state : int or None
            Random seed for reproducibility (default: None)
        """
        if n_splits < 2:
            raise ValueError
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state

    def split(self, X: np.ndarray, y: np.ndarray = None):
        """
        Generate train/validation indices for each fold.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            Training data
        y : array-like, shape (n_samples,), optional
            Target values (not used in basic K-Fold)

        Yields:
        -------
        train_idx : ndarray
            Training set indices for current fold
        val_idx : ndarray
            Validation set indices for current fold
        """
        if self.random_state is not None:
            np.random.seed(self.random_state)
        n_samples = len(X)
        indices = np.arange(n_samples)
        if self.shuffle:
            np.random.shuffle(indices)
        folds = np.array_split(indices, self.n_splits)
        for i in range(self.n_splits):
            val = folds[i]
            train = np.concatenate([folds[j] for j in range(self.n_splits) if j != i])
            yield train, val

    def cross_val_score(self, model: object, X: np.ndarray, y: np.ndarray, scoring: str = "r2") -> np.ndarray:
        """
        Evaluate model using cross-validation.

        Parameters:
        -----------
        model : estimator object
            Model with fit() and predict() methods
        X : array-like, shape (n_samples, n_features)
            Training data
        y : array-like, shape (n_samples,)
            Target values
        scoring : str
            Metric to use: 'r2', 'mse', 'mae'

        Returns:
        --------
        scores : ndarray, shape (n_splits,)
            Score for each fold
        """
        scores = []
        for train, val in self.split(X):
            X_train, y_train = X[train], y[train]
            X_val, y_val = X[val], y[val]
            model.fit(X_train, y_train)
            pred = model.predict(X_val)
            if scoring == "r2":
                scores.append(1 - np.mean((y_val - pred) ** 2) / np.mean((y_val - np.mean(y_val)) ** 2))
            if scoring == "mse":
                scores.append(-np.mean((y_val - pred) ** 2))
            if scoring == "mae":
                scores.append(-np.mean(np.abs(y_val - pred)))
        return np.array(scores)
