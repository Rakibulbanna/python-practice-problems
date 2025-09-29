# Problem-3: Implement an LRU Cache (Least Recently Used)
# Simulate caching in a backend system. You need to implement a cache with get() and put() methods.
class LRUCacheNode:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []  # List of (key, value) tuples

    def print_cache(self):
        print("cache__", self.cache)

    def get(self, key):
        # Find the item in the cache
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                # Move to end (most recently used)
                item = self.cache.pop(i)
                self.cache.append(item)
                return v
        return -1

    def put(self, key, value):
        # Check if key already exists
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                # Update existing key and move to end
                self.cache.pop(i)
                self.cache.append((key, value))
                return

        # Key doesn't exist, add new item
        if len(self.cache) >= self.capacity:
            # Remove least recently used (first item)
            self.cache.pop(0)

        # Add new item to end
        self.cache.append((key, value))


cache = LRUCacheNode(2)
# Put some items
cache.put(1, 10)  # Cache is {1: 10}
cache.put(2, 20)  # Cache is {1: 10, 2: 20}
print(cache.print_cache())
print("-" * 20)

# Get an item
print(f"get(1) -> Returns: {cache.get(1)}")
print(cache.print_cache())
print("-" * 20)

# Put another item, which will cause eviction
cache.put(3, 30)  # Evicts key 2 (the LRU item). Cache is {1: 10, 3: 30}
print(cache.print_cache())
print("-" * 20)

# Get the evicted item
print(f"get(2) -> Returns: {cache.get(2)}")

# =====================================================
# Solution 2 - using OrderedDict
# =====================================================
# import collections
# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}
#         self.order = []

#     def get(self, key):
#         if key in self.cache:
#             self.order.remove(key)
#             self.order.append(key)
#             return self.cache[key]
#         return -1

#     def put(self, key, value):
#         if key in self.cache:
#             self.order.remove(key)
#         self.cache[key] = value
#         self.order.append(key)
#         if len(self.cache) > self.capacity:
#             oldest = self.order.pop(0)
#             del self.cache[oldest]

# class LRUCache:

#     def __init__(self, capacity: int):

#         self.cache = collections.OrderedDict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:

#         if key not in self.cache:
#             return -1
#         else:
#             self.cache.move_to_end(key)
#             return self.cache[key]

#     def put(self, key: int, value: int) -> None:

#         if key in self.cache:
#             self.cache[key] = value
#             self.cache.move_to_end(key)
#         else:
#             if len(self.cache) >= self.capacity:
#                 self.cache.popitem(last=False)

#             self.cache[key] = value


# cache = LRUCache(2)
# print("Cache initialized with capacity 2.\n")

# # Put some items
# cache.put(1, 10)  # Cache is {1: 10}
# print(f"put(1, 10) -> Cache content: {dict(cache.cache)}")

# cache.put(2, 20)  # Cache is {1: 10, 2: 20}
# print(f"put(2, 20) -> Cache content: {dict(cache.cache)}")
# print("-" * 20)

# # Get an item
# print(f"get(1) -> Returns: {cache.get(1)}")  # Returns 10. Item 1 is now most recent.
# print(f"Cache content after get(1): {dict(cache.cache)}")  # Cache is now {2: 20, 1: 10}
# print("-" * 20)

# # Put another item, which will cause eviction
# cache.put(3, 30)  # Evicts key 2 (the LRU item). Cache is {1: 10, 3: 30}
# print(f"put(3, 30) -> Evicts key 2. Cache content: {dict(cache.cache)}")
# print("-" * 20)

# # Get the evicted item
# print(f"get(2) -> Returns: {cache.get(2)}")  # Returns -1 because key 2 was evicted
# print(f"Cache content after get(2): {dict(cache.cache)}")
