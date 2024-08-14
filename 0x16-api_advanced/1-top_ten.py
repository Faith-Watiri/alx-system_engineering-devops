#!/usr/bin/python3
"""
queries  the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import json
import requests
    
def top_ten(subreddit):
    url = requests.get( "https://www.reddit.com/r/{}/about.json")
            .format(subreddit),
    headers = {
            "User-Agent": "Imaginary_Big_8292")
    params = (
            "limit": 10
            }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if url.status_code == 404:
        print("None")
        return
    results = response.json().get("data"
            [print(c.get("data").get("title")) for c in results.get("children")]

    
