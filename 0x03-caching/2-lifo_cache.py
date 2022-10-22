#!/usr/bin/python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Class LIFOCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        self.last_put = ""
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_put)
            print('DISCARD:', self.last_put)
        if key:
            self.last_put = key

    def get(self, key):
        """
        Must return the value
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
