"""Downloads data csv data from the web to a local filepath as a csv.
Usage: download_data.py --url=<url> --out_file=<out_file> 
 
Options:
<url>               URL from where to download the data (must be in standard csv format)
<out_file>          Path (including filename) of where to locally write the file

Example:
Python download_data.py --url='https://archive.ics.uci.edu/ml/machine-learning-databases/00451/dataR2.csv' --out_file='C:/data/raw/data.csv'

"""

import os
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)

data = pd.read_csv(opt['--url'], header=None)
try:
    data.to_csv(opt['--out_file'], index=False)
except:
    os.makedirs(os.path.dirname(opt['--out_file']))
    data.to_csv(opt['--out_file'], index=False)
