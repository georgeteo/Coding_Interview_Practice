'''
CCC 4.1: Write an algorithm to determine whether a binary tree is balanced.
Where "balanced" means no two branches have depth difference greater than one
'''
from binary_tree import binary_tree
def get_depth(bt):
    '''
    Time Complexity: O(N) in number of elements, O(log(n)) in depth
    Space Complexity: O(n) in depth
    '''
    if bt is None:
        ''' Base case'''
        return 0
    left_depth = get_depth(bt.left_child)
    right_depth = get_depth(bt.right_child)
    if left_depth is False or right_depth is False:
        return False
    elif abs(right_depth - left_depth) > 1:
        return False
    depth = max(left_depth, right_depth) + 1
    return depth

def is_balanced(bt):
    rv = get_depth(bt)
    if rv is False:
        return False
    return True

if __name__=="__main__":
    print "Test"
    bt = binary_tree(0,0, binary_tree(1,1), binary_tree(2,1))
    print "Should be true - is %r"%is_balanced(bt)
    bt.right_child.add_children(3,4)
    bt.right_child.right_child.add_children(5,6)
    print "Should be false - is %r"%is_balanced(bt)
