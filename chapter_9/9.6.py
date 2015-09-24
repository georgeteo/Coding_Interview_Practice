'''
CCC 9.6: Implement an algorithm to print all valid combinations of n-pairs
of parentheses.
'''
from Queue import Queue

def parentheses_generator(k):
    q = Queue()
    q.put("()")
    while not q.empty():
        node = q.get()
        if len(node) > 2*k:
            break
        yield node
        q.put("(" + node + ")")
        left = "()"+ node
        right = node + "()"
        q.put(left)
        if left != right:
            q.put(right)

def print_kpair_parentheses(k):
    for parentheses in parentheses_generator(k):
        if len(parentheses) == 2*k:
            print parentheses

if __name__=="__main__":
    print_kpair_parentheses(3)
