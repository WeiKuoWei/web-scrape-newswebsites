import time
import json
import concurrent.futures
import sys

from geturls import getURLS
from getarticles import articlestojson
from wayback_machine import getArchiveURL


START_YEAR = 2023
END_YEAR = 2023
current_time = time.time()
    
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
        # for i in range(5,6):
        #     # get archive urls with wayback machine
        #     getArchiveURL(sites[i]['url'], START_YEAR, END_YEAR, "data/"+sites[i]['name']+"/urls-wayback.csv")
        #     updateTime("getArchiveURL")

        # single thread
        for i in range(0,10):
            i = str(i)
            getURLS("urls-wayback.csv", "urls_uncleaned.csv", sites[i]['name'], sites[i]['base_url'])
            updateTime("getURLS")
        
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
apnews:
- 2023 1/1-6/26 all have the same urls
- 2023 only has 136 unique urls
- https://apnews.com/hub/us-news was the url used from 2020/09-2023/06
- https://apnews.com/us-news is the new one from 2023/06
- consider finding a substitute for this news website

rerun nypost
- only has urls from 2024/02-2024/03
- consider finding a substitute for this news website

bbc:
- https://www.bbc.com/news/us-canada is the new website from 2024
- https://www.bbc.com/news/world/us_and_canada is the one used from 2012-2023


'''