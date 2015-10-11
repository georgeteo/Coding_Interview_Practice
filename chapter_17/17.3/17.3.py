'''
Trivial Solution:
Time Compleixty: O(n)
Space Complexity: O(n)
'''

def n_factorial(n):
    if n == 1:
        return 1
    else:
        return n * n_factorial(n-1)

def count_zero(n):
    factorial = n_factorial(n)
    count = 0
    factorial_list = [int(x)  for x in list(str(factorial))]
    for i in factorial_list[::-1]:
        if i == 0:
            count += 1
        else:
            break
    return count

'''
Cleverer Solution
'''


if __name__=="__main__":
    print "5! is ", n_factorial(5)
    print "5! has {} zeroes".format(count_zero(5))
