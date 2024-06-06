#!/usr/bin/python3
"""created a module that accpets a subreddit as a parameter returns the number
of subscriber"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
             Returns 0 if the subreddit does not exist or if there is an error.

    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditClient/1.0)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            res = response.json()
            return res['data']['subscribers']
        else:
            return 0

    except requests.exceptions.RequestException:
        return 0
