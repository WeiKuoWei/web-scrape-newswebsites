import time
import sys

from geturls import getURLS
# from geturls_bbc import getURLS
# from geturls_cnn import getURLS
# from geturls_dailymail import getURLS
# from geturls_foxnews import getURLS
# from geturls_huffpost import getURLS
# from geturls_nypost import getURLS
# from geturls_nytimes import getURLS
# from geturls_reuters import getURLS
# from geturls_washingtontimes import getURLS

from getarticles import articlestojson
from wayback_machine import getArchiveURL


START_YEAR = 2023
END_YEAR = 2023

site = {
    0:{
        "name":"bbc",
        "url":"https://www.bbc.com/news/us-canada"
    },
    1:{
        "name":"cnn",
        "url":"https://edition.cnn.com/us"
    },
    2:{
        "name":"dailymail",
        "url":"https://www.dailymail.co.uk/ushome/index.html"
    },
    3:{
        "name":"foxnews",
        "url":"https://www.foxnews.com/category/us"
    },
    4:{
        "name":"huffpost",
        "url":"https://www.huffpost.com/news/us-news"
    },
    5:{
        "name":"nypost",
        "url":"https://nypost.com/us-news/"
    },
    6:{
        "name":"nytimes",
        "url":"https://www.nytimes.com/section/us"
    },
    7:{
        "name":"reuters",
        "url":"https://www.reuters.com/world/us/"
    },
    8:{
        "name":"washingtonpost",
        "url":"https://www.washingtonpost.com/national/"
    },
    9:{
        "name":"washingtontimes",
        "url":"https://www.washingtontimes.com/news/national/"
    },
    20:{
        "name":"apnews",
        "url":"https://apnews.com/us-news"
    }

}

current_time = time.time()

def updateTime(function_name=""):
    global current_time

    end_time = time.time()
    print("Total time taken for {0} : {1}s".format(function_name, (end_time - current_time)))
    current_time = end_time


def main():
    print("Program started")
    
    try:
        for i in range(1,2):
            # get archive urls with wayback machine
            getArchiveURL(site[i]['url'], START_YEAR, END_YEAR, "data/"+site[i]['name']+"/urls-wayback.csv")
            updateTime("getArchiveURL")

        # # get urls from news
        # getURLS("urls-wayback.csv", "urls_uncleaned.csv", site[1]['name'])
        # updateTime("getURLS")

        # # clean urls
        # cleanURLS(site[1]+"urls_uncleaned.csv", site[1]+"urls_cleaned.csv")
        # updateTime("cleanURLS")

        # # get articles
        # articlestojson(site[1]+"/urls_cleaned.csv")
        # updateTime("articlestojson")
    
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

bbc:
- https://www.bbc.com/news/us-canada is the new website from 2024
- https://www.bbc.com/news/world/us_and_canada is the one used from 2012-2023
'''