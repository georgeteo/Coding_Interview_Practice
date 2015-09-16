'''
CCC 3.4: Tower of Hanoi
'''

'''
Lets use a python list append and pop to handle the stack.
Makes life easier
 '''

from pprint import pprint

def tower_solver(tower_set, start, spare, end):
    stack_to_move = tower_set[start]
    if len(stack_to_move) == 1:
        one_ring = stack_to_move.pop()
        tower_set[end].append(one_ring)
        return tower_set
    else:
        biggest_ring = stack_to_move[0]
        tower_set[start].pop(0)
        # Move top n-1 rings to spare
        tower_set_moved = tower_solver(tower_set, start, end, spare)
        # Move biggest ring to end
        tower_set_moved[end].append(biggest_ring)
        # Move n-1 rings to end
        tower_set_moved = tower_solver(tower_set_moved, spare, start, end)
        return tower_set_moved

if __name__ == "__main__":
    '''
    Q: Correct, but cant recurse more than 3 elements. Why?
    '''
    tower_set = [[3,2,1], [], []]
    pprint(tower_set)
    tower_solver(tower_set, 0, 1, 2)
    pprint(tower_set)
