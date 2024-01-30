#!/usr/bin/python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.__stats = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.__stats[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_key = min(self.__stats, key=self.__stats.get)
                del self.cache_data[min_key]
                del self.__stats[min_key]
                print("DISCARD: {}".format(min_key))
            self.__stats[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key not in self.cache_data:
            return None
        self.__stats[key] += 1
        return self.cache_data[key]
