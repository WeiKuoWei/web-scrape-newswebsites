import pandas as pd
import numpy as np
import os

# current_dir = os.getcwd()

# print(current_dir)

# data_dir = os.path.join(current_dir, 'fox-news/data')
# csv_dir = os.path.join(data_dir, 'urls.csv')

# open the csv file from data
df = pd.read_csv('data/urls.csv')

# find the number of rows in the dataframe
number_of_rows = df.shape[0]

# create a new column in the dataframe called 'label' and fill it with NaN values
df['label'] = ''

# if the entries in the 'URL' column contain the word video, set the 'label' column to 'video' 
# else, set the 'label' column to 'article'
df.loc[df['URL'].str.contains('video'), 'label'] = 'video'
df.loc[~df['URL'].str.contains('video'), 'label'] = 'article'

# save the dataframe to a new csv file
df.to_csv('data/urls_cleaned.csv', index=False)