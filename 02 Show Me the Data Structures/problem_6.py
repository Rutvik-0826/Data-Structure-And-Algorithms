class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        node = Node(value)
        self.size += 1

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def size(self):
        return self.size

    def values(self):
        """
        Return a list of the values contained in the linked list.

        :return: A list of values.
        """

        def recurse(node, values):
            if node is None:
                return values
            values.append(node.value)
            return recurse(node.next, values)

        return recurse(self.head, [])


def make_linked_list(values):
    """
    Create a linked list from a list of values.

    :param values: A list of values.
    :return: A linked list.
    """
    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)
    return linked_list


def union(list_a, list_b):
    """
    Create a new linked list containing the full set of values from both lists.

    :param list_a: A linked list.
    :param list_b: Another linked list.
    :return: A beautiful union of linked lists.
    """
    all_values = list_a.values()
    all_values.extend(list_b.values())
    return make_linked_list(set(all_values))


def intersection(list_a, list_b):
    """
    Create a new linked list containing values common to both lists.

    :param list_a: A linked list.
    :param list_b: Another linked list.
    :return: A splendid intersection of linked lists.
    """
    set_a = set(list_a.values())
    set_b = set(list_b.values())

    # Ensure we loop over the shorter set.
    if len(set_a) > len(set_b):
        set_a, set_b = set_b, set_a

    common = [x for x in set_a if x in set_b]
    return make_linked_list(common)


# =====================================================================
# TESTS
# =====================================================================
list_a = LinkedList()
list_a.append('a')
list_a.append('b')
list_a.append('c')

list_b = LinkedList()
list_b.append('a')
list_b.append('b')
list_b.append('d')

list_c = LinkedList()
list_c.append('e')
list_c.append('f')

assert ['a', 'b', 'c'] == list_a.values()
assert ['a', 'b', 'd'] == list_b.values()
assert ['e', 'f'] == list_c.values()

assert ['a', 'b', 'c', 'd'] == sorted(union(list_a, list_b).values())
assert ['a', 'b', 'c', 'e', 'f'] == sorted(union(list_a, list_c).values())
assert ['a', 'b', 'd', 'e', 'f'] == sorted(union(list_b, list_c).values())

assert ['a', 'b'] == sorted(intersection(list_a, list_b).values())
assert [] == intersection(list_a, list_c).values()
assert [] == intersection(list_b, list_c).values()

# Empty LinkedList tests
assert ['a', 'b', 'c'] == sorted(union(list_a, LinkedList()).values())
assert [] == intersection(list_a, LinkedList()).values()

assert [] == union(LinkedList(), LinkedList()).values()
assert [] == intersection(LinkedList(), LinkedList()).values()
