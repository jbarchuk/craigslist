#!/usr/bin/env python3

from craigslist import search

async for post in search('washingtondc', 'apa', postal=20071, search_distance=1):
    print(post)