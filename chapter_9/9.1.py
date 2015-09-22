'''
CCC 9.1: A child is running up a staircase with n steps and can hop either
1, 2, or 3 steps at a time. Implement a method to count how many possible ways
a child can run up the stairs.
'''
from Queue import Queue
def step_generator_1():
    ''' BFS corecursion
    But no way of stopping.'''
    q = Queue()
    q.put(0)
    while not q.empty():
        ''' Dangerous, can run infinite loop'''
        accmulated_value = q.get()
        q.put(accmulated_value + 1)
        q.put(accmulated_value + 2)
        q.put(accmulated_value + 3)
        yield accmulated_value

def step_generator_2(n):
    '''BFS corecursion
    But accumulate lists for paths'''
    q = Queue()
    q.put((0,))
    while not q.empty():
        '''Stop when [0,1,1,1,1...,1] that sums to n'''
        acc_value = q.get()
        q.put(acc_value + (1,))
        q.put(acc_value + (2,))
        q.put(acc_value + (3,))
        yield acc_value
        if sum(acc_value) == n+1 and len(acc_value) == n + 2:
            break


def number_of_ways_counter(n):
    count = 0
    for acc_value in step_generator_2(n):
        if sum(acc_value) == n:
            count += 1
    return count

if __name__=="__main__":
    print "Expected 1 - got ", number_of_ways_counter(1)
    print "Expected 2 - got ", number_of_ways_counter(2)
    print "Expected 4 - got ", number_of_ways_counter(3)
