'''
In python, stacks are natively supported in the list data type using append()
and pop().

Here, we implement python stacks using our linked list implementation.
'''

import linked_list

class stack(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        '''
        Push data onto the top of the stack
        '''
        new_node = linked_list.single_node(data)
        new_node.next = self.head
        self.head = new_node

    def peek(self):
        '''
        Peek at the top of the stack without removing it.
        '''
        return self.head.data

    def pop(self):
        '''
        Pop and return the top of the stack
        '''
        popped_head = self.head
        self.head = popped_head.next
        return popped_head.data
