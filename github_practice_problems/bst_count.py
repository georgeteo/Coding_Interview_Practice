def bst_count(node):
    '''
    DFS stack and BFS queue trivial. Just add to a counter.
    We implement DFS recursion here.
    '''
    if node.left is None and node.right is None:
        return 1
    if not node.left:
        left_counter = bst_count(node.left)
    else:
        left_counter = 0
    if not node.right:
        right_counter = bst_count(node.right)
    else:
        right_counter = 0
    return left_counter + right_counter + 1
    
