class Node:
    """
    Node(value = None, last = None, next = None)
    This is a base class containing a description of the queue node, stack or deque.
    A node consists of a value, a link to the previous element, and a link to the next element"""
    def __init__(self, value = None, last = None, next = None):
        self.value = value
        self.last = last
        self.next = next