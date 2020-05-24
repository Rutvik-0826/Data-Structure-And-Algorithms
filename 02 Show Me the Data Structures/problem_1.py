from collections import OrderedDict


class ZeroLengthCache(Exception):
    pass


class LeastRecentlyUsedStack(object):
    def __init__(self):
        self.items = OrderedDict()

    def is_empty(self):
        """Return a boolean indicating whether the stack is empty"""
        return len(self.items) == 0

    def pop(self):
        """Return the least recently used item"""
        return None if self.is_empty() else self.items.popitem(last=False)[0]

    def push(self, value):
        """Add an item to the LRU stack"""
        if value in self.items:
            self.items.pop(value)
        self.items[value] = value
        return self


class LeastRecentlyUsedCache(object):
    def __init__(self, capacity):
        if capacity < 1:
            raise ZeroLengthCache()

        self.capacity = capacity
        self.cache = dict()
        self.lru = LeastRecentlyUsedStack()

    def contains(self, key):
        """Return a boolean indicating whether an item with the given key exists in the cache"""
        return key in self.cache

    def is_full(self):
        """Return a boolean indicating whether the cache is full"""
        return len(self.cache) >= self.capacity

    def get(self, key):
        """Retrieve an item with the given key from the cache"""
        if self.contains(key):
            self.lru.push(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        """Add the given key / value pair to the cache"""
        if self.is_full():
            lru_key = self.lru.pop()
            if lru_key is not None:
                del self.cache[lru_key]

        self.lru.push(key)
        self.cache[key] = value


# -------------------
# Tests for LRU stack
# -------------------
stack = LeastRecentlyUsedStack()
stack.push('a')
stack.push('b')
stack.push('c')
stack.push('b')     # Repeat value. LRU order should now be ['a', 'c', 'b']

assert stack.is_empty() is False
assert stack.pop() == 'a'
assert stack.pop() == 'c'
assert stack.pop() == 'b'

# An empty stack returns None
assert stack.is_empty() is True
assert stack.pop() is None

# -------------------
# Tests for LRU cache
# -------------------
cache = LeastRecentlyUsedCache(5)

# Retrieve an item from the empty cache
assert cache.get('nope') == -1

cache.set('a', 1)
cache.set('b', 2)
cache.set('c', 3)
cache.set('d', 4)
cache.set('e', 5)

# If an item exists in the cache, it is returned
assert cache.get('b') == 2
assert cache.get('a') == 1

# A missing item returns -1
assert cache.get('z') == -1

# Adding an item to a full cache removes the least recently used item ('c')
cache.set('f', 6)
assert cache.get('f') == 6
assert cache.get('c') == -1

# Update a cached value
cache = LeastRecentlyUsedCache(3)
cache.set('a', 1)
assert cache.get('a') == 1

cache.set('a', 2)
assert cache.get('a') == 2

# Create a zero-length cache
try:
    cache = LeastRecentlyUsedCache(0)
    assert False, 'Attempting to create a zero-length cache should raise a ZeroLengthCache exception'
except ZeroLengthCache:
    assert True
