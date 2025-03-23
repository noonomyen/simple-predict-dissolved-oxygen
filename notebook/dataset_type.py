from dataclasses import dataclass
from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler
from numpy import ndarray

__all__ = ["Dataset"]

@dataclass
class Dataset:
    X: DataFrame
    y: DataFrame

    X_train: ndarray
    X_val: ndarray
    X_test: ndarray
    y_train: ndarray
    y_val: ndarray
    y_test: ndarray

    X_scaler: MinMaxScaler
    y_scaler: MinMaxScaler

    X_train_mms: ndarray
    X_val_mms: ndarray
    X_test_mms: ndarray
    y_train_mms: ndarray
    y_val_mms: ndarray
    y_test_mms: ndarray
