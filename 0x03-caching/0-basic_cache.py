#!/usr/bin/python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache that inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """
        Must assign to the dictionary
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Must assign to the dictionary
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
