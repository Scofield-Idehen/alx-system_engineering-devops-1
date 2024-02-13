#!/usr/bin/python3
''' returns a listt articles  '''
import pprint
import requests

url = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[], next_page=None):
    ''' list containing the titles of all hot articles '''
    headers = {'User-agent': 'sandy-app2'}
    params = {'limit': 100}

    if isinstance(next_page, str):
        if next_page != "DONE":
            params['after'] = next_page
        else:
            return hot_list

    response = requests.get(url.format(subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    next_page = data.get('after', 'DONE')
    if not next_page:
        next_page = "DONE"
    hot_list = hot_list + [item.get('data', {}).get('title')
                           for item in data.get('children', [])]
    return recurse(subreddit, hot_list, next_page)
