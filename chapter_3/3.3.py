'''
CCC 3.3: Implement a stack that overflows to a new stack at a certain height

Follow up: implement pop_at(k), which will pop from stack k.
'''

from stack import stack
from linked_list import single_node

class stack_with_length(stack):
    def __init__(self, head=None):
        self.length = 1 if head else 0
        super(stack_with_length, self).__init__(head)

    def push(self, data):
        super(stack_with_length, self).push(data)
        self.length += 1

    def pop(self):
        popped_head = self.head
        self.head = popped_head.next
        if popped_head is not None:
            self.length -= 1
        return popped_head


class set_of_stacks(object):
    def __init__(self, head_node=None, stack_height=0):
        first_stack = stack_with_length(head_node)
        self.set_of_stacks = [first_stack]
        self.stack_height_limit = stack_height

    def push(self, data):
        n = self.set_of_stacks[-1].length
        if n > self.stack_height_limit:
            new_node = single_node(data)
            new_stack = stack_with_length(new_node)
            self.set_of_stacks.append(new_stack)
        else:
            self.set_of_stacks[-1].push(data)

    def pop(self):
        popped_node = self.set_of_stacks[-1].pop()
        if self.set_of_stacks[-1].length == 0:
            self.set_of_stacks.pop()
        return popped_node.data

if __name__ == "__main__":
    first_node = single_node(1)
    ss = set_of_stacks(first_node, 2)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    print "Test"
    print "There should be two stacks"
    print "There are %d stacks\n"%len(ss.set_of_stacks)
    rv = ss.pop()
    print "Expected 5, Popped %d"%rv
    print "There should be two stacks"
    print "There are %d stacks\n"%len(ss.set_of_stacks)
    rv = ss.pop()
    print "Expected 4, Popped %d"%rv
    print "There should be one stacks"
    print "There are %d stacks\n"%len(ss.set_of_stacks)
