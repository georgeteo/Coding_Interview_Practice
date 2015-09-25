'''
Review:
XOR is associative.
0 XOR x = x
x XOR x = 0
'''

def find_uncoupled(array):
    acc = 0
    for x in array:
        acc ^= x
    return acc
