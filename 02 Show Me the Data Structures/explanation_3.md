# Problem 3: Huffman Coding #

## Encoding ##
Encoding uses several data structures as part of encoding process:

1. A map to store the frequency of each character.
2. A sorted list to store the character nodes.
3. A map to store the encoding for each character.
4. A binary tree (linked list) to store the Huffman tree.

The process of converting the list of sorted nodes to a binary tree uses the sorted list [2], and a separate queue to store the "combined" nodes. Using this approach, the time complexity for building a Huffman tree from a list of nodes sorted by frequency is `O(n)`. The alternative approach of using a single queue, which is sorted every time two nodes are combined, takes `O(n log n)`.

It should be noted, however, that the list still needs to be sorted once, using Python's built-in `sorted` function. This has a time complexity of `O(n log n)`.

Worst-case space efficiency is calculated as follows:

- `O(n)` for the frequency map.
- `O(n)` for the sorted list.
- `O(n/2)` for the "combined nodes" list.
- `O(2n -1)` for the binary tree. 

Therefore, the worst-case space efficiency is `O(n)`.

## Decoding ##
Decoding requires an encoded string, and a Huffman tree. Both the time efficiency and the space efficiency are `O(log n)`.
