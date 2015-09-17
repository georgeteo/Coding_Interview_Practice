'''
CCC 4.4: Design an algorithm that turns a binary tree into a linked list by level
'''
from binary_tree import binary_tree

def make_linked_list(bt):
    '''
    BFS:
    Time Complexity: O(V + E)
    Space Complexity: O(V)

    traversal_queue is a queue represented by a list
    linked_lists is a list of linked lists represented by a list of lists
    '''
    traversal_queue = []
    linked_lists = []
    linked_lists.append([bt.id])
    traversal_queue.append((bt.left_child, True))
    traversal_queue.append((bt.right_child, False))
    for node in traversal_queue:
        if node[0] is None:
            continue
        if node[1] is True:
            traversal_queue.append((node[0].left_child, True))
            linked_lists.append([node[0].id])
            traversal_queue.append((node[0].right_child, False))
        else:
            traversal_queue.append((node[0].left_child, False))
            linked_lists[-1].append(node[0].id)
            traversal_queue.append((node[0].right_child, False))
    return linked_lists

if __name__ == "__main__":
    bt = binary_tree(0, 0, binary_tree(1,1), binary_tree(2,1))
    ll = make_linked_list(bt)
    print ll
