"""authors: Aditya Bhatraju and Saule Atymtayeva

date: 2020-11-28

This script takes the training data file and saves a trained model
Usage: fit_cancer_prediction.py --in_train_file=<in_file> --out_file=<out_file> --out_file2=<out_file2> --model=<model>

Options:
<in_train_file>     Path (including filename and extension) from which train file is chosen
<out_file>          Path (including filename and extension) of where to locally write the file
<out_file2>         Path (including filename and extension) of where to locally write the file
<model>             Path (including filename and extension) of where to locally write the file

Example: Python fit_cancer_prediction.py --in_train_file='../data/raw/train.csv' --out_file='../src/classifiers_cv_scores.csv'
 --out_file2='../src/random_search_results.csv' --model='../results/trained_model.sav'
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
    RandomizedSearchCV,
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
import pickle
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

opt = docopt(__doc__)
in_train_file = opt['--in_train_file']
out_file = opt['--out_file']
out_file2 = opt['--out_file2']
model = opt['--model']

warnings.filterwarnings('ignore')

train_df = pd.read_csv(in_train_file)

# Separating X and y from train_df
X_train, y_train = train_df.drop(columns=["Classification", "Unnamed: 0"]), train_df["Classification"]

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
pd.DataFrame(results_dict, index = scores.keys()).round(4).to_csv(out_file)

# Making pipeline with LogisticRegression and optimizing `C`
pipe_lr = make_pipeline(LogisticRegression(max_iter=1000))

param_grid = {"logisticregression__C": 10.0 ** np.arange(-3, 3)}

random_search = RandomizedSearchCV(
    pipe_lr,
    param_grid,
    n_iter=50,
    verbose=1,
    n_jobs=-1,
    cv = 10,
    random_state=123,
    return_train_score=True,
)

random_search.fit(X_train, y_train);

print("Best hyperparameter values: ", random_search.best_params_)
print("Best score: %0.3f" % (random_search.best_score_))

pd.DataFrame(random_search.cv_results_)[
    [
        "mean_test_score",
        "param_logisticregression__C",
        "mean_fit_time",
        "rank_test_score",
    ]
].set_index("rank_test_score").sort_index().round(4).to_csv(out_file2)

# Fitting the best estimator of `LogisticRegression` on train dataset
trained_model = random_search.best_estimator_
trained_model.fit(X_train, y_train)

# Saving the trained model
pickle.dump(trained_model, open((model), 'wb'))