#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
from functools import wraps
import requests
import redis
from typing import Callable

re = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Get method that counting
    """

    @wraps(method)
    def wrapper(url):
        """
        Decorator
        """
        re.incr(f"count:{url}")
        cached = re.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')

        html = method(url)
        re.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    uses the requests module to obtain the HTML content
    """
    req = requests.get(url)
    return req.text
