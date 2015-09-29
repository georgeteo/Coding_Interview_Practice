def bst_height(node):
    '''BFS queue or DFS stack requires storing (node, level) pairs in data structure
    And keeping a max depth counter as you go along.
    Most natural with recursion'''
    if node == None:
        return 0
    left_height = bst_height(node.left)
    right_height = bst_height(node.right)
    return max(left_height, right_height) + 1
    
