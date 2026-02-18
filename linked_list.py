class Node:
    def __init__(self, value):
        self.value = value  # type
        self.next = None  # node


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.length: int = 0
