import pandas as pd

# open urls_uncleaned.csv
df = pd.read_csv('urls_uncleaned.csv', header=None, encoding='utf-8')

# Drop rows where the length of the second column is shorter than 10 characters
df = df[df[1].str.len() >= 10]

# sort the rows based on the value of the first column in ascending order
df.sort_values(by=0, ascending=True, inplace=True)

# Drop the duplicates
df.drop_duplicates(subset=[1], inplace=True)  # Assuming the second column has index 1

# save the cleaned dataframe to urls_cleaned.csv
df.to_csv('urls_cleaned.csv', header=None, index=False)

