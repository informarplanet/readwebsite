# Read website data 
# using reaquest urllib5

import requests
import urllib.request

# Get url content
# 
def readUrl(): 
    link='https://www.google.com' # passing url
    content=requests.get(link)

    # save content in a file
    contentData = urllib.request.urlopen(link)
    webdata= contentData.read()
    with open('website data.html','wb') as file:
        file.write(webdata)
    # save content into a file
readUrl()