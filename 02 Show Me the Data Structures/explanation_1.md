# Problem 1: LRU Cache #
Solution uses two main data structures:

1. A stack for tracking the most recently-used item, implemented as an OrderedDict.
2. A map for storing the cache key / value pairs.
   A map affords efficient access to a value, based on its unique identifier (key).
   
The time efficiency of the stack "set" and "get" operations is typically `O(1)`.

Neither the map (cache) nor the stack will grow beyond the specified maximum number of items, `n`. The space efficiency is therefore `O(2n)`.

