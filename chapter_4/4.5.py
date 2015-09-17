'''
CCC 4.5: Implement a function to determine if a binary tree is a binary search tree
'''
from binary_tree import binary_tree

def is_bst(bt):
    '''
    Recursively check tree is constructed corrected
    '''
    if bt is None:
        return (True, None, None)
    ''' Check left side '''
    if bt.left_child is not None:
        left_value = is_bst(bt.left_child)
        if bt.left_child.id <= bt.id:
            if left_value[0] is True:
                if (left_value[2] <= bt.id) or (left_value[2] is None):
                    left_truth = True
        else:
            left_truth = False
    else:
        left_value = [True, None, None]
        left_truth = left_value[0]
    ''' Check right side '''
    if bt.right_child is not None:
        right_value = is_bst(bt.right_child)
        if bt.right_child.id > bt.id:
            if right_value[0] is True:
                if (right_value[1] > bt.id) or (right_value[1] is None):
                    right_truth = True
        else:
            right_truth = False
    else:
        right_value = [True, None, None]
        right_truth = right_value[0]
    ''' Return type '''
    truth = left_truth & right_truth
    if left_value[1] is not None:
        minimum = min(left_value[1], bt.id)
    else:
        minimum = None
    if right_value[2] is not None:
        maximum = max(right_value[2], bt.id)
    else:
        maximum = None
    return (truth, minimum, maximum)

if __name__ == "__main__":
    bt = binary_tree(1,0,binary_tree(0,1), binary_tree(2,1))
    print "Test"
    print "Print should be true - is ", is_bst(bt)[0]
