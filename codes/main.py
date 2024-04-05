import time
import json
import concurrent.futures
import sys

from geturls import getURLS
from getarticles import articlestojson
from wayback_machine import getArchiveURL


# START_YEAR = 2023
# END_YEAR = 2023
current_time = time.time()
site_list = ["bbc", "cnn","foxnews","nationalreview","nytimes"]    

def updateTime(function_name=""):
    global current_time

    end_time = time.time()
    print("Total time taken for {0} : {1}s".format(function_name, (end_time - current_time)))
    current_time = end_time

def fetch_urls(site):
    getURLS("urls-wayback.csv", "urls_uncleaned.csv", site['name'], site['base_url'])
    updateTime("getURLS for " + site['name'])

def main():
    print("Program started")
    # Load the data from the JSON file
    with open('sites.json', 'r') as f:
        sites = json.load(f)
        
    try:
        for site in site_list:
            url_num = len(sites[site]['url'])
            for i in range(url_num):
                i = str(i)
                url_link = sites[site]['url'][i]["link"]
                start_year = sites[site]['url'][i]["start_year"]
                end_year = sites[site]['url'][i]["end_year"]
                export_csv_name = "data/"+site+"/urls-wayback.csv"

                # get archive urls with wayback machine
                getArchiveURL(url_link, start_year, end_year, export_csv_name)
                
                # print("Getting archive urls for", url_link, "from", start_year, "to", end_year)
                # print("Exporting to", export_csv_name)

                updateTime("getArchiveURL")

        # # single thread
        # for i in range(0,10):
        #     i = str(i)
        #     getURLS("urls-wayback.csv", "urls_uncleaned.csv", sites[i]['name'], sites[i]['base_url'])
        #     updateTime("getURLS")
        
        # # multi-thread attempt
        # # Extract the site data for the first 10 sites
        # site_data = [sites[str(i)] for i in range(4)]

        # # Use ThreadPoolExecutor to execute fetch_urls in parallel
        # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        #     executor.map(fetch_urls, site_data)

        # # get articles
        # for i in range(0,10):
        #     i = str(i)
        #     articlestojson(sites[i]+"/urls_cleaned.csv")
        #     updateTime("articlestojson")
    
    except Exception as e:
        print("Error: ", e)

    print("Program ended")

if __name__ == "__main__":
    main()


# 1812 articles for 1761 seconds
# roughly 25% of the urls are video urls

# notes

'''

'''