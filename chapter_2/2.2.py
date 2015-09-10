'''
CCC 2.2: Implement an algorithm to find the kth to last element in a linked list
'''
import linked_list

def trivial_solution(linked_list, k):
    '''
    O(n)
    '''
    # Get length of linked list.
    # Better: store length as a class variables
    node = linked_list.first
    length = 0
    while node:
        length += 1
        node = node.next

    node = linked_list.first
    counter = 0
    while counter < length - k:
        node = node.next
    return node

def runner_solution(linked_list, k):
    '''
    O(n)
    '''
    lead_node = linked_list.first
    lead_cnt = 0
    while lead_node:
        lead_cnt += 1
        lead_node = lead_node.next
        if lead_cnt = k:
            trailing_node = link_list.first
        if lead_cnt > k:
            trailing_node = trailing_node.next
    return trailing_node
