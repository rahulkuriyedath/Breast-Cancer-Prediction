"""Takes a csv file and outputs test dataset and train dataset to requested directory

Usage: split_train_test.py --in_train_file=<in_train_file> --train_out=<train_out> --test_out=<test_out>
 
Options:
<in_train_file>  Path and file name (with) from where to download the data (must be in standard csv format)
<train_out>      Name of zip file to be created (must be string with .zip extension)
<test_out>       Path (including filename) of where to locally write the file
"""

import pandas as pd
import os
from sklearn.model_selection import train_test_split

from docopt import docopt
opt = docopt(__doc__)

in_train_file = opt['--in_train_file']
train_out = opt['--train_out']
test_out = opt['--test_out']

  

raw_data = pd.read_csv(in_train_file)
train_df, test_df = train_test_split(raw_data, train_size = 0.8, random_state = 123)

try:
    train_df.to_csv(train_out)
    test_df.to_csv(test_out)
except:
    os.makedirs(os.path.dirname(train_out))
    train_df.to_csv(train_out)
    test_df.to_csv(test_out)


print('Successfully created train.csv and test.csv in the data/raw directory')