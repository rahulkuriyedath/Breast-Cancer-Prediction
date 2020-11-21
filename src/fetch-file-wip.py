
import os
import time
import requests
import pandas as pd
from zipfile import ZipFile 

os.chdir('/')                  # Go to root folder
os.mkdir('farm')           # Create a directory named farm in root
os.chdir('farm')            #Change directory from root to farm
os.mkdir('data')           # Create a directory named data in farm
os.chdir('data')             #Change directory from farm to data
os.mkdir('raw')             # Create a directory named raw in data
os.chdir('raw')               #Change directory from data to raw
op_path = os.getcwd() # put current working directory into a variable; 
#os.chdir(op_path)


url = 'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'
r = requests.get(url, allow_redirects=True) # Fetch the data from URL

time.sleep(5)  

with open('project_files2.zip', 'wb') as file:          # Open zip file named project_files2 and write fetched content to disk
    file.write(r.content)
file_name = "project_files2.zip"

time.sleep(5) 

with ZipFile(file_name, 'r') as zip:               # Extract the zip file to get csv files
    zip.printdir() 
    print('Extracting all the files in the zipped file') 
    zip.extractall() 
    print('Extracted') 

# Read to CSV
df2 = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_1678576.csv', encoding='iso-8859-1',skiprows=4)
df2
