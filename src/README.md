# Overview
===========

This folder consists of code documents required to run this project. 


# HOW TO NAVIGATE THIS FOLDER:
=============================


* `download_data.py`: """This script downloads data csv data from the web to a local filepath as a csv.

`Usage: download_data.py --url=<url> --out_file=<out_file>` 
 
Options:
<url>               URL from where to download the data (must be in standard csv format)
<out_file>          Path (including filename) of where to locally write the file

Example: Python download_data.py --url='https://archive.ics.uci.edu/ml/machine-learning-databases/00451/dataR2.csv' --out_file='C:/data/raw/data.csv'
"""


* `split_train_test.py`: """This script takes a csv file and outputs test dataset and train dataset to requested directory

`Usage: split_train_test.py --in_train_file=<in_train_file> --train_out=<train_out> --test_out=<test_out>`

Options:
<in_train_file>  Path and file name (with) from where to download the data (must be in standard csv format)
<train_out>      Name of zip file to be created (must be string with .zip extension)
<test_out>       Path (including filename) of where to locally write the file
"""


* `generate_figs.py`: """This scripts takes in the training data file as a csv and performs an exploratory data analysis

`Usage: Python generate_figs.py --in_train_file=<in_train_file> --figure_1=<figure_1>  --figure_2=<figure_2>`
 
Options:
<in_train_file>     Path (including filename and extension) from which train file is chosen
<figure_1>          Relative Path (including filename and extension) to where figure 1 is saved
<figure_2>          Relative Path (including filename with a . before the path and extension) to where figure 2 is saved

Example: Python generate_figs.py  --figure_1='/figures/class_imbalance_check.png'  --figure_2='./figures/pairplot.png'
"""


* `fit_cancer_prediction.py`: """This scripts takes the training and test data files and returns the test metric results of predictive models

`Usage: fit_cancer_prediction.py --in_train_file=<in_file> --in_test_file=<in_test_file>  --out_file=<out_file>` 
 
Options:
<in_train_file>     Path (including filename and extension) from which train file is chosen
<in_test_file>      Path (including filename and extension) from which test file is chosen
<out_file>          Path (including filename and extension) of where to locally write the file

Example: Python fit_cancer_prediction.py --in_train_file='../data/raw/train.csv' --in_test_file='../data/raw/test.csv'
         --out_file='../src/prediction_output.csv'
"""


* `EDA.ipynb`: This literate code document details the most recent analysis undertaken by group 16. 


