'''
CCC 3.5: Implement queue from 2 stacks
'''

from stack import stack_with_length
from linked_list import single_node

class queue_from_stack(object):
    def __init__(self):
        self.stack1 = stack_with_length()
        self.stack2 = stack_with_length()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        if self.stack2.peek() is None:
            '''
            If stack 2 is empty, need to transfer from stack1 to stack2
            '''
            node = self.stack1.pop()
            while node:
                self.stack2.push(node.data)
                node = self.stack1.pop()
        return self.stack2.pop()

if __name__ == "__main__":
    my_queue = queue_from_stack()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    one = my_queue.dequeue()
    print "Test"
    print "Expect: 1 - Got: %d"%one.data
    two = my_queue.dequeue()
    print "Expected: 2 - Got: %d"%two.data
