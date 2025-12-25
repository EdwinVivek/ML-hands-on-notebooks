# simple_pipeline.py
from sklearn import datasets
from sklearn import svm
import pandas as pd

def digits_df() -> pd.DataFrame:
    """Load the digits dataset."""
    digits = datasets.load_digits()
    _digits_df = pd.DataFrame(digits.data) 
    _digits_df["target"] = digits.target
    return _digits_df

def digits_model(digits_df: pd.DataFrame) -> svm.SVC:
    """Train a model on the digits dataset."""
    clf = svm.SVC(gamma=0.001, C=100.)
    _digits_model = clf.fit(
          digits_df.drop('target', axis=1), 
          digits_df.target
    )
    return _digits_model

def predicted_digits(
       digits_model: svm.SVC, 
       input_digits: pd.DataFrame) -> pd.Series:
    """Predict the digits."""
    return pd.Series(digits_model.predict(input_digits))

def input_digits() -> pd.DataFrame:
    digits = datasets.load_digits()
    _digits_df = pd.DataFrame(digits.data).sample(5)
    return _digits_df