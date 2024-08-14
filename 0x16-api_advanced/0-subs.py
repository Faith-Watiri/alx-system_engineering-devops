#!/usr/bin/python3
"""
function that queries  the Reddit API and returns
the number of subscribers for a given subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    url = requests.get("https://www.reddit.com/r/{}/about.json")
                    .format(subreddit), headers={"User-Agent": "Imaginary_Big_8292"}
    if url.status_code == 200:
        return url.json().get("data").get("subscribers")
    else:
        return 0
