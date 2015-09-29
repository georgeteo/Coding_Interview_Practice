''''
Reverse linked list by flipping pointers
'''
def reverse_linked_list(linked_list):
    last_node = linked_list
    this_node = last_node.next
    while this_node:
        next_node = this_node.next
        this_node.next = last_node
        last_node = this_node
        this_node = next_node
        
