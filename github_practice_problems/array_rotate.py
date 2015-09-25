'''
Problem: rotate an array by n to the right
'''

'''
Solution 1: O(n) time, O(n) space.
'''
def solution_1(array, k):
    n = len(array)
    new_array = [None] * n
    for i, element in array:
        new_array[(i+k)&n] = element
    return new_array

'''
Solution 2: O(n*k) time, O(1) space
'''
def solution_2(array, k):
    ''' Inplace'''
    while k > 0:
        temp = array[0]
        for i, element in enumerate(array[1:]):
            array[i] = element
        array[-1] = temp
        k -= 1

'''
Solution 3: O(n) time, O(1) space.

Find GCD of n and k, number elements by GCD: 1,2,3,1,2,3,... and swap groupwise.
'''

# To do: implementation.         
