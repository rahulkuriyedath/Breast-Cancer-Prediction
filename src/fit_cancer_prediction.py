"""authors: Aditya Bhatraju and Saule Atymtayeva

date: 2020-11-28

This scripts takes the training and test data files and returns the test metric results of predictive models
Usage: fit_cancer_prediction.py --in_train_file=<in_file> --in_test_file=<in_test_file>  --out_file=<out_file> 
 
Options:
<in_train_file>     Path (including filename and extension) from which train file is chosen
<in_test_file>      Path (including filename and extension) from which test file is chosen
<out_file>          Path (including filename and extension) of where to locally write the file

Example: Python fit_cancer_prediction.py --in_train_file='../data/raw/train.csv' --in_test_file='../data/raw/test.csv'
         --out_file='../src/prediction_output.csv'
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
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

opt = docopt(__doc__)
in_train_file = opt['--in_train_file']
in_test_file = opt['--in_test_file']
out_file = opt['--out_file']

warnings.filterwarnings('ignore')

train_df = pd.read_csv(in_train_file)
test_df = pd.read_csv(in_test_file)

# Separating X and y from train_df

X_train, y_train = train_df.drop(columns=["Classification"]), train_df["Classification"]

# Separating X and y from test_df

X_test, y_test = test_df.drop(columns=["Classification"]), test_df["Classification"]

# Identifying different feature types

numeric_features = X_train.select_dtypes(include=np.number).columns.tolist()
numeric_features

# Defining preprocessor

numeric_transformer = make_pipeline(StandardScaler())   # Since there is no missing values we do not need impute the data

preprocessor = make_column_transformer(
    (numeric_transformer, numeric_features)
)

preprocessor.fit(X_train);             # Calling fit to examine all the transformers
preprocessor.named_transformers_

# Using different classifiers

classifiers = {
    "DummyClassifier": DummyClassifier(strategy="most_frequent"),
    "Decision tree": DecisionTreeClassifier(),
    "kNN": KNeighborsClassifier(),
    "RBF SVM": SVC(),
    "Naive Bayes": BernoulliNB(),
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
}

results_dict = {}
results = {}

scoring = ['recall', 'accuracy', 'precision', 'f1']

for name, classifier in classifiers.items():
    pipe_classifier = make_pipeline(preprocessor, classifier)
    scores = cross_validate(pipe_classifier, X_train, y_train, return_train_score=True, scoring=scoring)
    results = {name: pd.DataFrame(scores).mean().tolist()}
    results_dict.update(results)
pd.DataFrame(results_dict, index = scores.keys()).round(2).to_csv(out_file)