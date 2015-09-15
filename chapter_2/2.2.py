'''
CCC 2.2: Implement an algorithm to find the kth to last element in a linked list
'''
from linked_list import single_node, singly_linked_list

def trivial_solution(linked_list, k):
    '''
    O(n)
    '''
    # Get length of linked list.
    # Better: store length as a class variables
    node = linked_list.head
    length = 0
    while node:
        length += 1
        node = node.next

    node = linked_list.head
    counter = 0
    while counter < length - k:
        node = node.next
        counter += 1
    return node

def runner_solution(linked_list, k):
    '''
    O(n)
    '''
    lead_node = linked_list.head
    lead_cnt = 0
    while lead_node:
        lead_cnt += 1
        lead_node = lead_node.next
        if lead_cnt == k:
            trailing_node = linked_list.head
        if lead_cnt > k:
            trailing_node = trailing_node.next
    return trailing_node

def recursive_solution(node, k):
    if node is None:
        return (0, node)
    next_node = node.next
    count, returned_node = recursive_solution(next_node, k)
    if count == k:
        return (count, returned_node)
    else:
        count += 1
        return (count, node)

if __name__ == "__main__":
    print "Test"

    head = single_node(1)
    linked_list = singly_linked_list(head)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.add(5)
    linked_list.add(6)

    print "Input List: %s"%str(linked_list)

    print "Expected output: 2"

    trivial_soln = trivial_solution(linked_list, 2).data
    print "Trivial Solution: %d"%trivial_soln
    runner_soln = runner_solution(linked_list, 2).data
    print "Runner Solution: %d"%runner_soln
    recursive_soln = recursive_solution(linked_list.head, 2)[1].data
    print "Recursive Solution: %d"%recursive_soln
