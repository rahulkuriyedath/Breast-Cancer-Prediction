"""authors: Aditya Bhatraju and Saule Atymtayeva

date: 2020-12-04

This script takes the training model and returns and predictions on the test dataset and a confusion matrix
Usage: test_cancer_prediction.py --in_test_file=<in_file> --in_model=<in_model> --out_matrix=<out_matrix> --out_table=<out_table>

Options:
<in_test_file>      Path (including filename and extension) which the csv test file is chosen from
<in_model>          Path (including filename and extension) which the trained model is chosen from
<out_matrix>        Path (including filename and extension) where to write the confusion matrix locally
<out_table>         Path (including filename and extension) where to write the prediction table locally

Example: Python fit_cancer_prediction.py --in_test_file='../data/raw/test.csv' --in_model='../results/trained_model.sav'
--out_matrix='../src/confusion_matrix.png' --out_table='../src/prediction_table.png'
"""
from docopt import docopt
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import pickle
import dataframe_image as dfi
from sklearn.metrics import (
    confusion_matrix,
    plot_confusion_matrix,
)

opt = docopt(__doc__)
in_test_file = opt['--in_test_file']
in_model = opt['--in_model']
out_matrix = opt['--out_matrix']
out_table = opt['--out_table']

test_df = pd.read_csv(in_test_file)

# Separating X and y from test_df
test_df = test_df.drop(columns=["Unnamed: 0"])
X_test, y_test = test_df.drop(columns=["Classification"]), test_df["Classification"]

# Predicting on the test dataset
trained_model = pickle.load(open(in_model, 'rb'))
predict_score = trained_model.score(X_test, y_test)
print("Prediction score on the test dataset: %0.3f" % (predict_score))

# Displaying confusion matrix
confusion_matrix = confusion_matrix(y_test, trained_model.predict(X_test))
print(confusion_matrix)

# Plotting confusion matrix
plot_confusion_matrix(trained_model, X_test, y_test, 
                             display_labels=["Healthy", "Patients"],
                             values_format="d", cmap=plt.cm.Blues)
plt.title('Confusion matrix')
plt.savefig(out_matrix)

# Saving predictions in a table
predictions = pd.Series(trained_model.predict(X_test))
predict_table = test_df
predict_table['Prediction'] = predictions
predict_table.dfi.export(out_table, table_conversion='matplotlib')

print("The confusion matrix and prediction table are successfully created")