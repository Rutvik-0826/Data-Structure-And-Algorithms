import hashlib
import time


class Node(object):
    def __init__(self, block):
        self.block = block
        self.next = None


class Blockchain(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, block_data):
        """
        Add a new block containing the given data to the blockchain.

        :param block_data: The block data.
        :return: None
        """
        previous_hash = None if self.tail is None else self.tail.block.hash
        node = Node(Block(time.time(), block_data, previous_hash))

        if self.tail is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def search(self, target_hash):
        """
        Search the blockchain for a block identifed by the given hash.

        :param target_hash: The hash we're searching for.
        :return: The block data, or None if no matching block is found.
        """
        def recurse(current_node):
            if current_node is None:
                return None
            if current_node.block.hash == target_hash:
                return current_node.block.data
            return recurse(current_node.next)

        return recurse(self.head)


class Block(object):
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calculate_hash()

    def _calculate_hash(self):
        """
        Calculate the hash of this Block instance.

        :return: string
        """
        sha = hashlib.sha256()
        string_to_hash = str(self.timestamp) + self.data + str(self.previous_hash)
        hashed_string = string_to_hash.encode()
        sha.update(hashed_string)
        return sha.hexdigest()


chain = Blockchain()
chain.append('The first block')
chain.append('The second block')

assert isinstance(chain.head, Node)
assert isinstance(chain.head.block, Block)
assert chain.head.block.data == 'The first block'
assert chain.head.block.previous_hash == None

assert chain.head.next.block.data == 'The second block'
assert chain.head.next.block.previous_hash == chain.head.block.hash

assert chain.search(chain.tail.block.hash) == 'The second block'
assert chain.search('nope') is None
