from collections import deque
import sys


class Node(object):
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left_child = None
        self.right_child = None


class HuffmanEncoder(object):
    @staticmethod
    def _build_frequency_map(string):
        """
        Build a character -> frequency map for a string.

        :param string: The subject string.
        :return: dict
        """

        def recurse(letters, map):
            if len(letters) == 0:
                return map

            letter, *tail = letters
            map[letter] = map[letter] + 1 if letter in map else 1
            return recurse(tail, map)

        return recurse(list(string), {})

    @staticmethod
    def _convert_map_to_nodes(map):
        """
        Convert a frequency map to a list of Nodes.

        :param map: A frequency map.
        """
        return [Node(character, frequency) for character, frequency in map.items()]

    @staticmethod
    def _sort_nodes(nodes):
        """
        Sort a list of Nodes by frequency.

        :param nodes: A list of Nodes.
        """
        return sorted(nodes, key=lambda t: t.frequency)

    @staticmethod
    def _dequeue_lowest_frequency_node(list_a, list_b):
        """
        Dequeue the Node with the lowest frequency from the start of the given queues.

        :param list_a: A deque of Nodes.
        :param list_b: A deque of Nodes.
        :return: A tuple containing list_a, list_b, and the extracted Node.
        """
        if not len(list_a):
            node = list_b.popleft()
        elif not len(list_b):
            node = list_a.popleft()
        else:
            node = list_a.popleft() if list_a[0].frequency <= list_b[0].frequency else list_b.popleft()
        return list_a, list_b, node

    @staticmethod
    def _build_tree(nodes):
        """
        Build a Huffman tree from a sorted list of Nodes.

        :param nodes: A list of Nodes, sorted by frequency.
        :return Node: The root node of a Huffman tree.
        """

        def recurse(leaves, combined):
            if len(leaves) + len(combined) == 1:
                if len(combined) == 0:
                    # Single-item tree. This seems very inelegant.
                    node = leaves.popleft()
                    root = Node(None, node.frequency)
                    root.left_child = node
                    combined.append(root)
                    return recurse(leaves, combined)
                else:
                    return combined.popleft()

            # Retrieve the two lowest-frequency nodes.
            leaves, combined, node_a = HuffmanEncoder._dequeue_lowest_frequency_node(leaves, combined)
            leaves, combined, node_b = HuffmanEncoder._dequeue_lowest_frequency_node(leaves, combined)

            # Create the parent node, with the combined frequency.
            parent = Node(None, node_a.frequency + node_b.frequency)
            parent.left_child = node_a
            parent.right_child = node_b

            # Add the new parent node to the "combined" deque
            combined.append(parent)

            return recurse(leaves, combined)

        return recurse(deque(nodes, len(nodes)), deque([], len(nodes)))

    @staticmethod
    def _build_character_encoding_map(huffman_tree):
        """
        Build a character -> encoding map for the given tree.

        :param tree: A Huffman tree.
        :return: dict
        """

        def recurse(node, encoding_map, code):
            if node.character:
                encoding_map[node.character] = code
            if node.left_child:
                encoding_map = recurse(node.left_child, encoding_map, code + '0')
            if node.right_child:
                encoding_map = recurse(node.right_child, encoding_map, code + '1')
            return encoding_map

        return recurse(huffman_tree, {}, '')

    @staticmethod
    def encode(string):
        """
        Encode the given string.

        :param string:
        :return: A tuple containing the encoded string, and the associated Huffman tree.
        """

        if not len(string):
            return None, None

        def recurse(string, encoding_map):
            if not string:
                return ''
            character, *tail = string
            return encoding_map[character] + recurse(tail, encoding_map)

        frequency_map = HuffmanEncoder._build_frequency_map(string)
        leaves = HuffmanEncoder._sort_nodes(HuffmanEncoder._convert_map_to_nodes(frequency_map))
        huffman_tree = HuffmanEncoder._build_tree(leaves)

        return (
            recurse(string, HuffmanEncoder._build_character_encoding_map(huffman_tree)),
            huffman_tree
        )


class HuffmanDecoder(object):
    @staticmethod
    def decode_character(encoded, huffman_tree):
        """
        Decode the first character from an encoded string.

        :param encoded: An encoded string.
        :param huffman_tree: A Huffman tree.
        :return: A tuple containing the decoded character, and the remaining encoded string.
        """

        def recurse(binary_path, node):
            if node.character:
                return node.character, binary_path
            if not binary_path:
                return '', binary_path  # This should never happen

            branch, *path = binary_path
            node = node.left_child if branch == '0' else node.right_child

            return recurse(path, node)

        return recurse(encoded, huffman_tree)

    @staticmethod
    def decode(encoded, huffman_tree):
        """
        Decode an encoded string.

        :param encoded: An encoded string.
        :param huffman_tree: A Huffman tree.
        :return: The decoded string.
        """

        def recurse(binary_path):
            if not binary_path:
                return ''
            character, binary_path = HuffmanDecoder.decode_character(binary_path, huffman_tree)
            return character + HuffmanDecoder.decode(binary_path, huffman_tree)

        return recurse(encoded)


def huffman_encoding(data):
    """
    Encode a string.

    :param data: The string to encode.
    :return: A tuple containing the encoded string, and the associated Huffman tree.
    """
    return HuffmanEncoder.encode(data)


def huffman_decoding(data, tree):
    """
    Decode a string, using a Huffman tree.

    :param data: The string to decode.
    :param tree: The Huffman tree used to encode the string.
    :return: The decoded string
    """
    return HuffmanDecoder.decode(data, tree)


# =====================================================================
# TESTS
# =====================================================================
# ------------------------------
# Test build_frequency_map
# ------------------------------
assert HuffmanEncoder._build_frequency_map('a') == {'a': 1}
assert HuffmanEncoder._build_frequency_map('aa') == {'a': 2}
assert HuffmanEncoder._build_frequency_map('abab') == {'a': 2, 'b': 2}
assert HuffmanEncoder._build_frequency_map('Aa') == {'A': 1, 'a': 1}
assert HuffmanEncoder._build_frequency_map('AAAAAA') == {'A': 6}


# ------------------------------
# Test convert_map_to_tuples
# ------------------------------
def test_convert_map_to_nodes(map, expected):
    result = HuffmanEncoder._convert_map_to_nodes(map)
    for i in range(len(expected)):
        assert expected[i].character == result[i].character
        assert expected[i].frequency == result[i].frequency


test_convert_map_to_nodes({'a': 1}, [Node('a', 1)])
test_convert_map_to_nodes({'a': 1, 'b': 2}, [Node('a', 1), Node('b', 2)])
test_convert_map_to_nodes({}, [])


# ------------------------------
# Test sort_tuple_list
# ------------------------------
def test_sort_nodes(nodes, expected):
    result = HuffmanEncoder._sort_nodes(nodes)
    for i in range(len(expected)):
        assert expected[i].character == result[i].character
        assert expected[i].frequency == result[i].frequency


test_sort_nodes([Node('a', 1)], [Node('a', 1)])
test_sort_nodes([Node('a', 2), Node('b', 1)], [Node('b', 1), Node('a', 2)])
test_sort_nodes([Node('a', 2), Node('b', 1)], [Node('b', 1), Node('a', 2)])
test_sort_nodes([], [])

# ------------------------------
# Test build_tree
# ..............................
# Expected tree:
#       (None, 4)
#           |
#   -----------------
#   |               |
# (c,2)         (None, 2)
#              ----------
#              |        |
#           (a, 1)    (b, 1)
# ------------------------------
result = HuffmanEncoder._build_tree([Node('a', 1), Node('b', 1), Node('c', 2)])

# Root node
assert isinstance(result, Node)
assert result.character is None
assert result.frequency is 4

assert isinstance(result.left_child, Node)
assert isinstance(result.right_child, Node)

# Left branch
assert result.left_child.character is 'c'
assert result.left_child.frequency is 2

# Right branch
assert result.right_child.character is None
assert result.right_child.frequency is 2

assert isinstance(result.right_child.left_child, Node)
assert isinstance(result.right_child.right_child, Node)

assert result.right_child.left_child.character is 'a'
assert result.right_child.left_child.frequency is 1

assert result.right_child.right_child.character is 'b'
assert result.right_child.right_child.frequency is 1

# Single item tree
result = HuffmanEncoder._build_tree([Node('A', 6)])

assert isinstance(result, Node)
assert result.character is None
assert result.frequency is 6
assert result.left_child.character is 'A'
assert result.left_child.frequency is 6

# ------------------------------
# Test build_character_map
# ------------------------------
tree = HuffmanEncoder._build_tree([Node('a', 1), Node('b', 1), Node('c', 2)])
result = HuffmanEncoder._build_character_encoding_map(tree)

assert result['a'] == '10'
assert result['b'] == '11'
assert result['c'] == '0'

# ------------------------------
# Test encode / decode
# ------------------------------
encoded, tree = HuffmanEncoder.encode('cabc')
assert encoded == '010110'
assert tree.left_child.character == 'c'
assert tree.right_child.left_child.character == 'a'
assert tree.right_child.right_child.character == 'b'

decoded = HuffmanDecoder.decode(encoded, tree)
assert decoded == 'cabc'

# Test with a string of identical characters
encoded, tree = HuffmanEncoder.encode('AAAAAAAA')
assert encoded == '00000000'
assert tree.left_child.character == 'A'

decoded = HuffmanDecoder.decode(encoded, tree)
assert decoded == 'AAAAAAAA'

# Test with an empty string
encoded, tree = HuffmanEncoder.encode('')
assert encoded is None
assert tree is None

# =====================================================================

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
