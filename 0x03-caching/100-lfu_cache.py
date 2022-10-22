#!/usr/bin/python3
"""
LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        self.counter = 0
        self.ages = {}
        self.used = {}
        super().__init__()

    def count_u(self, key):
        """
        Increases value
        """
        if key in self.used:
            self.used[key] += 1
        else:
            self.used[key] = 1

    def put(self, key, item):
        """
        Must assign to the dictionary
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used = min(self.used.values())
                for k, _ in sorted(self.ages.items(),
                                   key=lambda x: x[1]):
                    if self.used[k] == least_used:
                        self.cache_data.pop(k)
                        self.ages.pop(k)
                        self.used.pop(k)
                        break
                print('DISCARD:', k)
            self.ages[key] = self.counter
            self.counter += 1
            self.count_u(key)

    def get(self, key):
        """
        Must return the value
        """
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            self.count_u(key)
            return self.cache_data.get(key)
        return None
