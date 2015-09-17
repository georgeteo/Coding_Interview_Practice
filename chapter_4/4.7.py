'''
CCC 4.7: Design an algorithm to find the first common ancestor of a binary tree.

Solution: make path two two nodes into a list of left/right moves.
Then look at sequence of left, right moves.
Left/left or right/right the common ancestor until left/right difference.
'''
from binary_tree import binary_tree

def path_from_root(bt, node):
    ''' Base Cases '''
    if bt is None:
        return None
    if bt.id == node:
        return []
    ''' Recursive Step '''
    left_return_list = path_from_root(bt.left_child, node)
    right_return_list = path_from_root(bt.right_child, node)
    ''' Another Base Case'''
    if left_return_list is not None:
        return_list = left_return_list
        t = "Left"
    elif right_return_list is not None:
        return_list = right_return_list
        t = "Right"
    else:
        return None
    ''' Recursive Step continues '''
    return_list.insert(0, [bt, t])
    return return_list

def common_ancestor(bt_root, node1, node2):
    node1_path = path_from_root(bt_root,node1)
    node2_path = path_from_root(bt_root, node2)
    for i in range(min(len(node1_path), len(node2_path))):
        node1_element = node1_path[i]
        node2_element = node2_path[i]
        if node1_element[1] != node2_element[1]:
            return node1_element
    if len(node1_path) == len(node2_path):
        return None
    elif len(node1_path) < len(node2_path):
        return node1_path[-1]
    else:
        return node2_path[-1]



if __name__ == "__main__":
    bt = binary_tree(0, 0,
        binary_tree(1,1,
            binary_tree(3,2), binary_tree(4,2)),
        binary_tree(2,1,
            binary_tree(5,2), binary_tree(6,2)))
    print "Test"
    print "Expect 2 - got ",common_ancestor(bt, 5, 6)[0].id
