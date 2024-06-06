#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            res = response.json()
            return res['subscribers']
        else:
            return 0

    except requests.exceptions.RequestException:
        return 0
