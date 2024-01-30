#!/usr/bin/python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def __init__(self):
        """Initiliaze"""
        self.cache = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache[key] = item

    def get(self, key):
        """Get an item by key"""
        if key and key in self.cache:
            return self.cache[key]
        return None

    def print_cache(self):
        """Print the cache"""
        print("Current cache:")
        for key, item in sorted(self.cache.items()):
            print("{}: {}".format(key, item))
