#!/usr/bin/python3
"""lists top 10n hot posts of the subreddit"""

import json
import requests


def top_ten(subreddit):
    """
    Retrieves and lists the top 10 hot posts of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'YOUR_USER_AGENT'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        res = response.json()
        print('\n'.join([res['data']['children'][i]['data']['title']
                         for i in range(10)]))
    else:
        print(None)
