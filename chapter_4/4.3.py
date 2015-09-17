'''
Given a sorted list, generate the minimal depth bst
'''
from binary_search_tree import binary_search_tree as bst

def generate_minimal_bst(L):

    if len(L) == 3:
        top_node = bst(L[1], 0) # Depth = 0 for now
        top_node.add(L[0])
        top_node.add(L[2])
        return top_node
    half = len(L)/2
    left_half = L[:half]
    right_half = L[half + 1:]
    middle_node = bst(L[half], 0)
    left_node = generate_minimal_bst(left_half)
    right_node = generate_minimal_bst(right_half)
    middle_node.left_child = left_node
    middle_node.right_child = right_node
    return middle_node

if __name__ == "__main__":
    L=[1,2,3,4,5,6,7]
    bst = generate_minimal_bst(L)
    print "        " + str(bst.id)
    left_node = bst.left_child
    right_node = bst.right_child
    print "    " + str(left_node.id) + "        " + str(right_node.id)
    left_left = left_node.left_child
    left_right = left_node.right_child
    right_left = right_node.left_child
    right_right = right_node.right_child
    print " " + str(left_left.id) + "    " + str(left_right.id) + "    " + str(right_left.id) + "    " + str(right_right.id)
