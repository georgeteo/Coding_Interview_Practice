'''
Integer 123 is represented by 3->2->1

In place by writing over digit_2
'''

def sum(linked_list_1, linked_list_2):
    digit_1 = linked_list_1
    digit_2 = linked_list_2
    carry = 0
    while digit_1 or digit_2:
        if not digit_1:
            d1 = 0
        else:
            d1 = digit_1.data
        if not digit_2:
            d2 = 0
        else:
            d2 = digit_2.data

        s = d1 + d2 + carry
        if s > 9:
            r =  s - 10
            carry = 1
        else:
            r = s
            carry = 0
        digit_2.data = r
        digit_1 = digit_1.next
        digit_2 = digit_2.next
