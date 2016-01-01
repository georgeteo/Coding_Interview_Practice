def print_multiplication_table(n):
    row = range(1, n+1)
    for i in row:
        print [i*x for x in row]

if __name__=="__main__":
    print_multiplication_table(5)        
