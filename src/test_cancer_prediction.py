"""authors: Aditya Bhatraju and Saule Atymtayeva

date: 2020-12-04

This script takes the training model and returns a test score and predictions on test dataset
Usage: test_cancer_prediction.py --in_test_file=<in_file> --model=<model> --out_file=<out_file>

Options:
<in_test_file>      Path (including filename and extension) which the test file is chosen from
<model>             Path (including filename and extension) which the trained model is chosen from
<out_file>          Path (including filename and extension) where to locally write the file

Example: Python fit_cancer_prediction.py --in_test_file='../data/raw/test.csv' --model='../results/trained_model.sav'
--out_file='../src/prediction_table.csv'
"""
from docopt import docopt
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

opt = docopt(__doc__)
in_test_file = opt['--in_test_file']
model = opt['--model']
out_file = opt['--out_file']

test_df = pd.read_csv(in_test_file)

# Separating X and y from test_df
test_df = test_df.drop(columns=["Unnamed: 0"])
X_test, y_test = test_df.drop(columns=["Classification"]), test_df["Classification"]