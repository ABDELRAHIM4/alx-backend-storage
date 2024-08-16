#!/usr/bin/env python3
"""will implement a get_page function"""
import redis
import requests


def get_page(url: str) -> str:
    """will implement a get_page function"""
    use = redis.Redis()
    count = f"count:{url}"
    cash = f"cashe:{url}"
    if use.get(cash):
        return use.get(cash).decode('utf-8')
    res = requests.get(url)
    use.setex(cash, 10, res.txt)
    use.incr(count)
    return (res.txt)
