'''
George's implementatation of singly and doubly linked lists in Python
'''

class single_link_node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class double_link_node(single_link_node):
    def __init__(self, data, prev_node=None, next_node=None):
        self.previous = prev_node
        super(double_link_node, self).__init__(data, next_node)


class singly_linked_list:
    def __init__(self, node):
        self.head = node
        self.first = node

    def insert(self, data):
        new_node = single_link_node(data)
        self.head.next_node = new_node
        self.head = new_node

class doubly_linked_list(singly_linked_list):
    def __init__(self, node):
        self.previous = None
        super(doubly_linked_list, self).__init__(node)

    def insert(self, data):
        new_node = double_link_node(data, prev_node=self.head)
        self.head.next_node = new_node
        self.head = new_node
        
