import pandas as pd
import os

raw_data = pd.read_csv('../data/raw/dataR2.csv')
train_df, test_df = train_test_split(raw_data, train_size=0.8, random_state=123)

try:
    train_df.to_csv('../data/raw/train.csv')
    test_df.to_csv('../data/raw/test.csv')
except:
    os.mkdir('../data/raw/')
    train_df.to_csv('../data/raw/train.csv')
    test_df.to_csv('../data/raw/test.csv')
    
print('Successfully created train.csv and test.csv in the data/raw directory')