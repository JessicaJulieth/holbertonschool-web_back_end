#!/usr/bin/python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class FIFOCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_pop = sorted(self.cache_data)[0]
            self.cache_data.pop(to_pop)
            print('DISCARD:', to_pop)

    def get(self, key):
        """
        Must return the value
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
