'''
CCC 3.2: Design a stack with push, pop,and min in O(1) time.
'''

from linked_list import single_node
from stack import stack

'''
Node with min solution:
Min time complexity O(1)
Min space complexity O(N)
'''

class stack_node_with_min(single_node):
    def __init__(self, data=None, last_min=None):
        self.data = data
        if last_min is None:
            minimum = data
        elif data < last_min:
            minimum = data
        else:
            minimum = last_min
        self.min = minimum
        self.next = None

class stack_with_min(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        new_node = stack_node_with_min(data, self.head.min)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        popped_head = self.head
        self.head = popped_head.next
        return popped_head.data

    def min(self):
        return self.head.data

'''
Two stack solution:
Time complexity: O(1)
Space Complexity: O(N) but N likely to be smaller
'''
from stack import stack
from linked_list import single_node
class two_stack(object):
    def __init__(self, head=None):
        self.stack_head = head
        self.min_head = head

    def push(self, data):
        new_node = single_node(data)
        new_node.next = self.stack_head
        self.stack_head = new_node

        if data <= self.min_head.data:
            new_min = single_node(data)
            new_min.next = self.min_head
            self.min_head = new_min

    def pop(self):
        popped_head = self.stack_head
        self.stack_head = popped_head.next
        if popped_head.data <= self.min_head.data:
            self.min_head = self.min_head.next
        return popped_head

    def min(self):
        return self.min_head.data



if __name__ == "__main__":
    s = stack_with_min(stack_node_with_min(data=1))
    s.push(2)
    s.push(3)
    print "Test for solution 1:"
    print "Expected Min: 1"
    print "Min in stack: %d\n"%s.min()

    s = two_stack(single_node(1))
    s.push(2)
    s.push(3)

    print "Test for solution 2:"
    print "Expected Min: 1"
    print "Min in stack: %d"%s.min()
