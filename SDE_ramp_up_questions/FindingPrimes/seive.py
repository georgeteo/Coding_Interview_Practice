def sieve(n):
    lst = range(2,n)
    for p in lst:
        i = 2
        item = i * p
        while item in lst:
            lst.remove(item)
            item += p
    return lst

if __name__=="__main__":
    print sieve(10)
