'''
CCC 2.1:
1. Remove duplicates from an unsorted linked list.
We assume doubly lined list, but honestly does not matter.
2. Do it without temporary variables (TODO (georgeteo))
'''

from linked_list import single_node, singly_linked_list

def remove_duplicate_with_temp_var(linked_list):
    '''
    O(n)
    '''
    duplicates = dict()
    node = linked_list.head
    while node:
        if node.data in duplicates.keys():
            node.data = node.next.data
            node.next = node.next.next
        else:
            duplicates[node.data] = 1
        node = node.next

def remove_duplicates_no_temp_var(linked_list):
    pass

if __name__ == "__main__":
    print "Test"

    '''
    Making linked list
    2 -> 3 -> 2 -> 1
    '''

    head = single_node(1)
    linked_list = singly_linked_list(head)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(2)
    print "Input Linked List:%s"%str(linked_list)

    remove_duplicate_with_temp_var(linked_list)
    '''
    Expected result:
    2-> 3 -> 1
    '''
    print "Remove duplicates with temporary variables: %s"%str(linked_list)
