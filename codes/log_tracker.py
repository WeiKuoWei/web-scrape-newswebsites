import pandas as pd
import os

def exportLog(id, export_file_name, scrape_time, clean_time, status):
    file_path = "data/log/" + export_file_name
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=['id', 'scrape_time', 'clean_time', 'status'])
        df.to_csv(file_path, index=False)

    df = pd.read_csv(file_path, header=0)
    # append the new row to the dataframe
    df.loc[df.shape[0]] = [id, scrape_time, clean_time, status]
    df = df.sort_values(by='id', ascending=True)
    df.to_csv(file_path, index=False)

# exportLog(1, "log_cnn.csv", None, None, "fail")