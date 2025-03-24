from dataclasses import dataclass
from pandas import DataFrame, Series
from sklearn.preprocessing import MinMaxScaler
from numpy import ndarray

__all__ = ["Dataset"]

@dataclass
class Dataset:
    X: DataFrame
    y: Series

    X_train: ndarray
    X_val: ndarray
    X_test: ndarray
    y_train: ndarray
    y_val: ndarray
    y_test: ndarray
