'''
Given array and sum, return boolean of whether a pair of integers from the array can make sum.

What is the complexity?
'''

def target_sum(array, desired_sum):
    bottom = 0
    top = len(array) - 1
    while bottom <= top:
        s = array[bottom] + array[top]
        if s == desired_sum:
            return True
        elif s < desired_sum:
            bottom += 1
        elif s > desired_sum:
            top -= 1
    return False
