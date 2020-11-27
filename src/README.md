# Overview
===========

This folder consists of code documents required to run this project. 


# HOW TO NAVIGATE THIS FOLDER:
=============================

* `pop_farm_fetch.py`: This script downloads and saves the datasets used in this project by using the docopt Python package to create the command line argument functionality. 

This file takes zipped file from a URL, unzips it and chooses a zipped file as defined by user and writes that file to disk to a location specified by user.

Arguments:
link: URL that has .zip file
zip_file_name: Takes the name of zip file to be created on disk
out_file: Takes path where csv has to be written along with the file name of csv  
pop_farm: Choose data to be downloaded for population or farming. Takes 2 values: 'pop' or 'farm'
in_zip_file: Choose which of the zipped files you want to be outputted as csv

Example: Python pop_farm_fetch.py --link='http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv' --zip_file_name='tst.zip' --out_file='C:/outing.csv' --pop_farm=pop --in_zip_file='API_SP.POP.TOTL_DS2_en_csv_v2_1678576.csv'



* `EDA.ipynb`: This literate code document details an exploratory data analysis of the data sets group 16 has.  
