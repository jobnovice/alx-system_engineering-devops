#!/usr/bin/python3
"""
    Task 0
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ gets the number of subscribers """
    r = requests.get('https://api.reddit.com/r/{}/about.json'
                     .format(subreddit),
                     headers={'user-agent': 'ianscustomthing'},
                     allow_redirects=False)
    rj = r.json()
    if rj.get('message') == 'Not Found':
        return 0
    s = rj.get('data').get('subscribers')
    return s
