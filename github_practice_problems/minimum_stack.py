'''
Keep a second stack that keeps track of the minimum.

Add to minimum stack when new item <= current top of stack
Remove when item to be removed is <= top of stack

Time Complexity O(1)
Space Compexity O(n)
'''
class min_stack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def add(self, value):
        self.stack.append(value)

        try:
            minimum_value = self.min_stack[-1]
            if value <= minimum_value:
                self.min_stack.append(value)
        except IndexError:
            self.min_stack.append(value)

    def pop(self):
        try:
            top_of_stack = self.stack.pop()
        except IndexError:
            pass
        try:
            minimum_value = self.min_stack[-1]
            if top_of_stack <= minimum_value:
                self.min_stack.pop()
        except:
            pass
        return top_of_stack

    def peek(self):
        try:
            return self.stack[-1]
        except:
            pass

    def peek_min(self):
        try:
            return self.min_stack[-1]
        except:
            pass

    def print_stack(self):
        print self.stack

    def print_min_stack(self):
        print self.min_stack

if __name__ == "__main__":
    s = min_stack()
    print "Adding 2, 3, 1, 4"
    s.add(2)
    s.add(3)
    s.add(1)
    s.add(4)
    print "Stack: ", s.print_stack()
    print "Min stack should be: [2, 1]"
    print "Min stack is: ", s.print_min_stack()

    print ""
    print "Remove ", s.pop()
    print "Min stack should not have changed: ", s.print_min_stack()

    print ""
    print "Remove ", s.pop()
    print "Min stack should be changed: ", s.print_min_stack()
