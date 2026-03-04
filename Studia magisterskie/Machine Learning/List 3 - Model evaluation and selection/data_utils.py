"""
Data loading utilities for Model Selection lab.
"""

import os

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.datasets import fetch_california_housing, load_diabetes
from sklearn.preprocessing import StandardScaler


def load_california_housing() -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Load California Housing dataset (20,640 samples, 8 features).

    Features:
    - MedInc: Median income in block group
    - HouseAge: Median house age in block group
    - AveRooms: Average number of rooms per household
    - AveBedrms: Average number of bedrooms per household
    - Population: Block group population
    - AveOccup: Average number of household members
    - Latitude: Block group latitude
    - Longitude: Block group longitude

    Target: Median house value in $100,000s

    Returns
    -------
    X : ndarray, shape (20640, 8)
        Feature matrix (standardized)
    y : ndarray, shape (20640,)
        Target values
    """
    data = fetch_california_housing()
    X = data.data
    y = data.target

    # Standardize features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y


def load_boston_housing() -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Load Boston Housing dataset from CSV (506 samples, 13 features).

    Note: This dataset has ethical concerns regarding the 'B' feature.
    Consider using California Housing or synthetic data instead.

    Features include: CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS,
                      RAD, TAX, PTRATIO, B, LSTAT

    Target: Median value of owner-occupied homes in $1000s

    Returns
    -------
    X : ndarray, shape (506, 13)
        Feature matrix (standardized)
    y : ndarray, shape (506,)
        Target values
    """
    # Get path relative to this file
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    file_path = os.path.join(data_dir, "boston_housing.csv")

    df = pd.read_csv(file_path)
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Standardize features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y


def load_diabetes_data() -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Load Diabetes dataset (442 samples, 10 features).

    Features: age, sex, bmi, bp, s1-s6 (blood serum measurements)
    Target: Quantitative measure of disease progression one year after baseline

    Returns
    -------
    X : ndarray, shape (442, 10)
        Feature matrix (already standardized)
    y : ndarray, shape (442,)
        Target values
    """
    data = load_diabetes()
    X = data.data
    y = data.target

    return X, y
