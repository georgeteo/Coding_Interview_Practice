'''
Tail recursion factorial
'''
def tail_recursion_factorial(n, accumulator=1):
    ''' In practice, python will not optimize tail recursion'''
    if n < 0:
        return "Error"
    if n == 0:
        return 1
    return tail_recursion_factorial(n-1, accumulator*n)

'''Python version:
Do use imperative loop'''
def python_loop_factorial(n, acc=1):
    while True:
        if n == 0:
            return acc
        n, acc = n - 1, acc * n
