import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.storage.add_to_tail(ListNode(value))

    def pop(self):
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length