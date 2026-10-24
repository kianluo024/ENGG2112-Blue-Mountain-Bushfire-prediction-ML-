"""Small model-fitting functions; experiment runners own data selection."""

import warnings

import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from .data import model_matrix


def fit_logistic(training: pd.DataFrame, config: dict) -> Pipeline:
    """Fit preprocessing and logistic weights on training observations only."""
    predictors = model_matrix(training, config["feature_set"])
    labels = training.fire_positive.astype(int)
    if set(labels.unique()) != {0, 1}:
        raise ValueError("Both classes must occur in the training partition")
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(**config["logistic_regression"])),
    ])
    with warnings.catch_warnings():
        warnings.simplefilter("error", ConvergenceWarning)
        pipeline.fit(predictors, labels)
    return pipeline
