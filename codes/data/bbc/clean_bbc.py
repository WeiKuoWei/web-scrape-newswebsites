import pandas as pd

# # open urls_uncleaned.csv
# df = pd.read_csv('urls_uncleaned.csv', header=None, encoding='utf-8')

# # drop all the rows that do not contain 'us'
# df = df[df[0].str.contains('-us-')]

# # drop all the rows that contains /live/
# df = df[~df[0].str.contains('/live/')]

# # drop the all rows that contains live-report
# df = df[~df[0].str.contains('live-report')]

# # add a new column to the dataframe
# df['status'] = 'no'

# # save the cleaned dataframe to urls_cleaned.csv
# df.to_csv('urls_cleaned.csv', header=None, index=False)

df = pd.read_csv('urls_uncleaned.csv', header=None, encoding='utf-8')

# if the row only contains one column, insert a new column to index 0 with 0 as the value
for i in range(len(df)):
    if len(df.iloc[i]) == 1:
        df.iloc[i] = [0] + df.iloc[i].tolist()

df.to_csv('urls_uncleaned.csv', header=None, index=False)
