def fibonaci_generator():
    fib0 = 0
    yield fib0
    fib1 = 1
    yield fib1
    while True:
        fib2 = fib0+fib1
        yield fib2
        fib0,fib1 = fib1, fib2

def fibonaci_printer(k):
    for i, fibonaci in enumerate(fibonaci_generator()):
        if i > k:
            break
        print fibonaci
    
