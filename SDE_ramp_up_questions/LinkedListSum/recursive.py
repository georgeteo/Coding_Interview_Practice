'''
Integer 123 is 1->2->3

In place
'''

def recursive_sum(linked_list_1, linked_list_2):
    list_1_length = linked_list_1.length
    list_2_length = linked_list_2.length
    if list_1_length == list_2_length:
        d1 = linked_list_1.data
        d2 = linked_list_2.data
        if list_1_length == 1:
            s = d1 + d2
            if s > 9:
                r = s - 10
                carry = 1
            else:
                r = s
                carry = 0
            linked_list_2.data = r
            return carry
        else:
            c = recursive_sum(linked_list_1.next, linked_list_2.next)
            s = d1+d2+c
            if s > 9:
                r = s-10
                carry = 1
            else:
                r=s
                carry = 0
            linked_list_2.data = r
            return carry
    elif list_1_length > list_2_length:
        c = recursive_sum(linked_list_1.next, linked_list_2)
        s = linked_list_1.data + c
        if s > 9:
            r = s-10
            carry = 1
        else:
            r = s
            carry = 0
        linked_list_2.data = r
        return c
    else:
        c = recursive_sum(linked_list_1, linked_list_2.next)
        s = linked_list_2.data + c
        if s > 9:
            r = s-10
            carry = 1
        else:
            r = s
            carry = 0
        linked_list_2.data = r
        return c
