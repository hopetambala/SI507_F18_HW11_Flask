from secrets_example import *
import requests

def get_stories(section):
    baseurl = "https://api.nytimes.com/svc/topstories/v2/"

    extendedurl = baseurl + section + '.json'

    params={'api-key': api_key}

    return requests.get(extendedurl,params).json()

def get_headlines(nyt_results_dict):
    results = nyt_results_dict['results']
    headlines = []

    for r in results:
        title = r['title']
        url = r['url']
        #headlines.append(r['title'])
        headlines.append(str(title)+' ('+str(url)+')')
    return headlines