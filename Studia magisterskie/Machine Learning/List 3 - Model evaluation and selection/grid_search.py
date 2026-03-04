"""
Grid search module.
"""

import numpy as np


class KFoldCV:
    """
    K-Fold cross-validator.
    """

    def __init__(self, n_splits: int = 5, shuffle: bool = True, random_state: int = 42):
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
        if self.shuffle:
            self.random_state = np.random.RandomState(random_state)
        else:
            self.random_state = None

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
        n_samples = len(X)
        indices = np.arange(n_samples)
        if self.shuffle:
            self.random_state.shuffle(indices)
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


class GridSearchCV:
    """
    Grid Search with cross-validation.
    """

    def __init__(self, model: object, param_grid: dict, cv: int = 5, scoring: str = "r2"):
        """
        Initialize Grid Search with cross-validation.

        Parameters:
        -----------
        model : estimator object
            Model to tune (must have fit/predict methods)
        param_grid : dict
            Dictionary with parameter names (str) as keys and lists of
            parameter settings to try as values
        cv : int
            Number of cross-validation folds (default: 5)
        scoring : str
            Metric to optimize: 'r2', 'neg_mse', 'neg_mae'
        """
        self.model = model
        self.param_grid = param_grid
        self.cv = cv
        self.scoring = scoring

        self.best_params_ = None
        self.best_score_ = None
        self.best_model_ = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> "GridSearchCV":
        """
        Run grid search on all parameter combinations.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            Training data
        y : array-like, shape (n_samples,)
            Target values

        Returns:
        --------
        self : GridSearchCV
            Fitted grid search object
        """
        keys = list(self.param_grid.keys())
        vals = [np.array(self.param_grid[k]) for k in keys]
        grids = np.meshgrid(*vals, indexing="ij")
        combs = np.stack(grids, axis=-1).reshape(-1, len(keys))
        cv = KFoldCV(n_splits=self.cv)
        for comb in combs:
            params = {}
            for key, val_numeric in zip(keys, comb, strict=True):
                original_values = self.param_grid[key]
                if (
                    isinstance(original_values, (list, np.ndarray))
                    and original_values
                    and isinstance(original_values[0], bool)
                ):
                    params[key] = bool(val_numeric)
                else:
                    params[key] = val_numeric
            model = type(self.model)(**params)
            scores = cv.cross_val_score(model, X=X, y=y, scoring=self.scoring)
            mean_score = np.mean(scores)
            if self.best_score_ is None:
                self.best_score_ = float("-inf")
            if mean_score > self.best_score_:
                self.best_score_ = mean_score
                self.best_params_ = params
                self.best_model_ = type(self.model)(**params)
        self.best_model_.fit(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict using the best found parameters.

        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            Samples to predict

        Returns:
        --------
        y_pred : array-like, shape (n_samples,)
            Predictions
        """
        if self.best_model_ is None:
            raise RuntimeError
        return self.best_model_.predict(X)
