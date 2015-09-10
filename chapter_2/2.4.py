'''
Write code to partition a linked list around an element x, such that all elements
less than x are to the left and elements larger or equal to x are on the right
'''

def partition_linked_list(linked_list, x):
    '''
    O(n)

    Assumes that the left and right lists do not need to be sorted
    '''
    node = linked_list.first
    lesser_list_first = True
    greater_list_first = True
    while node:
        node_data = node.data
        if node_data == x:
            central_node = node
        elif node_data < x:
            if lesser_list_first: # Can make this a try, except control flow?
                lesser_list = doubly_linked_list(node)
                lesser_list_first = False
            else:
                lesser_list.insert(node_data)
        else:
            if greater_list_first:
                greater_list = doubly_linked_list(node)
                greater_list_first = False
            else:
                greater_list.insert(node_data)
        node = node.next
    central_node.previous = lesser_list.first
    central_node.next = greater_list.first
    return greater_list.head    
