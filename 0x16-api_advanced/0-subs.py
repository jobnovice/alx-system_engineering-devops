#!/usr/bin/python3
"""module deined for fetching the number of subscrbribers for a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/"

    try:
        response = requests.get(url, allow_redirects=False)

        res = response.json()

        return res['data']['subscribers']
    except requests.exceptions.RequestException as e:
        return 0
