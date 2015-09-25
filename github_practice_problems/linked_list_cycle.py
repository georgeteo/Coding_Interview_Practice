'''
Review: Two runner method. One pointer next, one pointer next.next.
'''

def has_cycle(linked_list):
    runner1 = linked_list.next
    runner2 = linked_list.next.next
    while runner1 and runner2:
        if runner1 == runner2:
            return False
        runner1 = runner1.next
        runner2 = runner2.next.next
    return True
