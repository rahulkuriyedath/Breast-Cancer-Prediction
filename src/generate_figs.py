"""authors: Ifeanyi Anene and Rahul

date: 2020-11-28
This scripts takes in the training data file as a csv and performs an exploratory data analysis
Usage: generate_figs.py --in_train_file=<in_train_file> --figure_1=<figure_1>  --figure_2=<figure_2> 
 
Options:
<in_train_file>     Path (including filename and extension) from which train file is chosen
<figure_1>          Relative Path (including filename and extension) to where figure 1 is saved
<figure_2>          Relative Path (including filename with a . before the path and extension) to where figure 2 is saved
Example: Python generate_figs.py  --figure_1='/figures/class_imbalance_check.png'  --figure_2='./figures/pairplot.png'
"""
from docopt import docopt
import os
import numpy as np
import pandas as pd


opt = docopt(__doc__)
in_train_file = opt['--in_train_file']
figure_1 = opt['--figure_1']
figure_2 = opt['--figure_2']


try:
    eda1 = train_df["Classification"].value_counts(normalize=True).plot(kind = 'bar').get_figure().savefig(figure_1) # working. relative path
    plot = sns.pairplot(train_df).savefig(figure_2)
except:
    os.mkdir("./figures")
    eda1 = train_df["Classification"].value_counts(normalize=True).plot(kind = 'bar').get_figure().savefig(figure_1) # working. relative path
    plot = sns.pairplot(train_df).savefig(figure_2)