"""Downloads data csv data from the web to a local filepath as a csv.

Usage: pop_farm_fetch.py --link=<link> --zip_file_name=<zip_file_name> --out_file=<out_file_> --pop_farm=<pop_farm> --in_zip_file=<in_zip_file>
 
Options:
<link>               URL from where to download the data (must be in standard csv format)
<zip_file_name>      Name of zip file to be created (must be string with .zip extension)
<out_file>           Path (including filename) of where to locally write the file
<pop_farm>           Choose --pop_farm = 'pop' for Population file or --pop_farm = 'farm' for Asia Farm Produce file;
<in_zip_file>        Choose the file name of the zipped files whose csv you want
"""

import time
import requests
import pandas as pd
from zipfile import ZipFile 

from docopt import docopt
opt = docopt(__doc__)

url = opt['--link']
zip_file= opt['--zip_file_name']
out= opt['--out_file']
farm_pop = opt['--pop_farm']
in_zip_file = opt['--in_zip_file']

url = url
r = requests.get(url, allow_redirects=True)

time.sleep(20) 

with open(zip_file, 'wb') as file:
    file.write(r.content)
file_name = zip_file

time.sleep(20) 

with ZipFile(file_name, 'r') as zip: 
    zip.printdir() 
    print('Extracting all the files in the zipped file') 
    zip.extractall() 
    print('Extracted')
if farm_pop == 'farm':
    df2 = pd.read_csv(in_zip_file, encoding='iso-8859-1')
    df2.to_csv(out, index=False) 

if farm_pop == 'pop':
    df2 = pd.read_csv(in_zip_file, encoding='iso-8859-1',skiprows=4)
    df2.to_csv(out, index=False) 