from newsplease import NewsPlease
import pandas as pd
import json
import csv

# NUMBER_OF_URLS = 10

def articlestojson(file_path, NUMBER_OF_URLS=10):
    # Initialize an empty list to store URLs from the CSV
    urls_list = []

    # Open the CSV file and read its contents into the list
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header if there is one
        for row in csv_reader:
            urls_list.append(row[0])  # Assumes single column CSV

    # Initialize a dictionary to serve as the buffer for article information
    articles_info = {}

    # Iterate over each URL, fetching the article data and storing it in the buffer
    for url in urls_list[:-1]:
        try:
            article = NewsPlease.from_url(url, timeout=5)
            # Use the URL as the key and the article's serializable dictionary as the value
            articles_info[url] = article.get_serializable_dict() if article else None
        except Exception as e:
            print(f"Error fetching article for URL {url}: {e}")
            articles_info[url] = None

    # Write the buffer (articles_info) to a JSON file
    with open("articles_info.json", "w", encoding='utf-8') as file:
        json.dump(articles_info, file, ensure_ascii=False, indent=4)

# Example usage
# process_csv_to_json('path_to_your_csv_file.csv')