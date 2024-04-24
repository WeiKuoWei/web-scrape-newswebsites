import pandas as pd

# open urls_uncleaned.csv
df = pd.read_csv('urls_uncleaned.csv', header=None, encoding='utf-8')

old_len = len(df)

# positive filtering
df = df[df[1].str.len() >= 60]
# df = df[df[1].str.contains("us")]

df_a = df[df[1].str.contains("/articles/technology")]
df_b = df[df[1].str.contains("/blogs/future_tense")]
df_c = df[df[1].str.contains("/blogs/bad_astronomy")]

# negative filtering
df = df[~df[1].str.contains("/topics/")]
df = df[~df[1].str.contains("/staff/")]
df = df[~df[1].str.contains("/subscribe/")]
df = df[~df[1].str.contains("/foryou/")]
df = df[~df[1].str.contains("/human-interest/")]
df = df[~df[1].str.contains("/content/")]
df = df[~df[1].str.contains("/culture/")]
df = df[~df[1].str.contains("/podcasts/")]
df = df[~df[1].str.contains("/authors.")]
df = df[~df[1].str.contains("/briefing/")]
df = df[~df[1].str.contains("/business/")]
df = df[~df[1].str.contains("/news-and-politics/")]
df = df[~df[1].str.contains("/news_and_politics/")]
df = df[~df[1].str.contains("/movies.")]
df = df[~df[1].str.contains("/blogs/")]
df = df[~df[1].str.contains("/articles/")]
df = df[~df[1].str.contains("/sidebars/")]

# combine dfs
df = pd.concat([df, df_a, df_b, df_c])




# sorting and duplicate removal
df["length"] = df[1].str.len()
df.sort_values(by="length", ascending=True, inplace=True)
df.drop(columns="length", inplace=True)

# Drop the duplicates
df.drop_duplicates(subset=[1], inplace=True)  # Assuming the second column has index 1

# print the number of rows
print("Total rows: ", len(df))
print("Removed: ", old_len - len(df))

# save the cleaned dataframe to urls_cleaned.csv
df.to_csv('urls_cleaned.csv', header=None, index=False)

