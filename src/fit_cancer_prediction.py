"""authors: Adithya and Saule Atymtayeva

date: 2020-11-28

"""
from docopt import docopt
import numpy as np
import pandas as pd
import warnings
from sklearn.compose import (
    ColumnTransformer,
    TransformedTargetRegressor,
    make_column_transformer,
)
from sklearn.model_selection import (
    cross_validate,
    train_test_split,
)
from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


train_df = pd.read_csv(in_train_file)
test_df = pd.read_csv(in_test_file)

# Separating X and y from train_df

X_train, y_train = train_df.drop(columns=["Classification"]), train_df["Classification"]

# Separating X and y from test_df

X_test, y_test = test_df.drop(columns=["Classification"]), test_df["Classification"]

# Identifying different feature types
