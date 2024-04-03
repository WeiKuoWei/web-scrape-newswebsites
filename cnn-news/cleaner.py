import pandas as pd
import numpy as np
import os

def cleanURLS(filepath):
    # open the csv file from data
    df = pd.read_csv(filepath)

    # find the number of rows in the dataframe
    number_of_rows = df.shape[0]

    # create a new column in the dataframe called 'label' and fill it with NaN values
    df['label'] = ''

    # if the entries in the 'URL' column contain the word video, set the 'label' column to 'video' 
    # else, set the 'label' column to 'article'
    df.loc[df['URL'].str.contains('video'), 'label'] = 'video'
    df.loc[~df['URL'].str.contains('video'), 'label'] = 'article'

    article_count = df[df['label'] == 'article'].shape[0]

    # prints the number of rows with the label 'article'
    print("The number of articles is: {}, which is {}% of the total ({}/{})".format(
    article_count,
    round(article_count/number_of_rows*100, 2),
    article_count,
    number_of_rows
    ))

    # drop the rows with the label 'video'
    df = df[df['label'] == 'article']

    # save the dataframe to a new csv file
    df.to_csv('../cnn-news/data/urls_cleaned.csv', index=False)