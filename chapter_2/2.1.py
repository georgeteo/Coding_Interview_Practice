'''
CCC 2.1:
1. Remove duplicates from an unsorted linked list.
We assume doubly lined list, but honestly does not matter.
2. Do it without temporary variables (TODO (georgeteo))
'''

import linked_list

def remove_duplicate_with_temp_var(linked_list):
    '''
    O(n)
    '''
    duplicates = dict()
    node = linked_list.first
    while node:
        try dict[node.data]:
            linked_list.remove(node)
        except KeyError:
            dict[node.data] = 1
        node = node.next
