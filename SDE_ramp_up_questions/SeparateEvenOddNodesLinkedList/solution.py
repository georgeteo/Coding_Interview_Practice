def separate_even_odd_nodes(linked_list_head):
    even = linked_list_head
    odd = linked_list_head.next
    i = 0
    node = odd
    even_last = even
    odd_last = odd
    while node:
        mod = i % 2
        if mod == 0:
            even_last.next = node
            node = node.next
            even_last = node
        else:
            odd_last.next = node
            node = node.next
            odd_last = node
