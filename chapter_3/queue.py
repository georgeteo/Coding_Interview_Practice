'''
Queue implementation via linked list:
- singly linked list with a pointer to the end

Double Ended Queue implementation:
- doubly linked list
- dynamically resizing array

Python native implementation:
- collections.deque
'''

import linked_list

class queue(object):
    '''
    Queue implemented as a singly linked list with a node at the back
    '''

    def __init__(self, head=None):
        self.tail = head
        self.head = head
        self.length = 1 if head else 0

    def enqueue(self, data):
        new_node = linked_list.single_node(data)
        if self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        popped_head = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return popped_head
