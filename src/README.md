# Overview
===========

This folder consists of code documents required to run this project. 


# HOW TO NAVIGATE THIS FOLDER:
=============================

* `download_data.py`: """This script downloads the data from the internet and saves it locally. 

Usage: Python generate_data.py --in_raw_data=<in_raw_data>  --train_df=<train_df> --test_df=<test_df>
Options:
<in_raw_data>           Path (including filename and extension)of raw data csv.
<train_df>              Path (including filename and extension) where the
<test_df>               Path (including filename and extension) of where to locally store the figure

Example:
    python src/generate_data.py --data_path="data/raw/raw_data_csv" --train_df="data/raw/train_csv" --test_df="data/raw/test_csv"
"""


* `generate_data.py`: """This script takes in the raw data and splits it into train and test data using 80/20 split.

Usage: Python generate_data.py --in_raw_data=<in_raw_data>  --train_df=<train_df> --test_df=<test_df>
Options:
<in_raw_data>           Path (including filename and extension)of raw data csv.
<train_df>              Path (including filename and extension) where the
<test_df>               Path (including filename and extension) of where to locally store the figure

Example:
    python src/generate_data.py --data_path="data/raw/raw_data_csv" --train_df="data/raw/train_csv" --test_df="data/raw/test_csv"
"""


* `generate_figs.py`: """This scripts takes in the training data file as a csv and performs an exploratory data analysis
Usage: generate_figs.py --in_train_file=<in_train_file> --figure_1=<figure_1>  --figure_2=<figure_2> 
 
Options:
<in_train_file>     Path (including filename and extension) from which train file is chosen
<figure_1>          Relative Path (including filename and extension) to where figure 1 is saved
<figure_2>          Relative Path (including filename with a . before the path and extension) to where figure 2 is saved
Example: Python generate_figs.py  --figure_1='/figures/class_imbalance_check.png'  --figure_2='./figures/pairplot.png'
"""


* `fit_cancer_prediction.py`: """This scripts takes the training and test data files and returns the test metric results of predictive models

Usage: fit_cance_prediction.py --in_train_file=<in_file> --in_test_file=<in_test_file>  --out_file=<out_file> 
 
Options:
<in_train_file>     Path (including filename and extension) from which train file is chosen
<in_test_file>      Path (including filename and extension) from which test file is chosen
<out_file>          Path (including filename and extension) of where to locally write the file
Example: Python fit_cancer_prediction.py --in_train_file='../data/raw/train.csv' --in_test_file='../data/raw/test.csv'
         --out_file='../src/prediction_output.csv'
"""



* `EDA.ipynb`: This literate code document details the most recent analysis undertaken by group 16. 


