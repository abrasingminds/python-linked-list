import pytest
from linked_list import Node, LinkedList


def test_node_and_linkedlist_creation():
    # Test Node creation
    node = Node(10)

    assert node.value == 10  # type(value) ==  dynamic,
    assert node.next is None  # type(next) == Node

    # Test LinkedList creation
    ll = LinkedList()  ## type(ll) == LinkedList

    assert ll.head is None
    assert ll.length == 0
