'''
Implment queue with two stacks.

One enqueue stack.
One dequeue stack: that dequeues stuff and loads from enqueue stack if empty.

Time Complexity: 
'''

class queue_from_stack(object):
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if not self.dequeue_stack:
            '''Transfer for enqueue stack'''
            while not self.enqueue_stack:
                temp = self.enqueue_stack.pop()
                self.dequeue_stack.append(temp)
        else:
            return self.deq.pop()
