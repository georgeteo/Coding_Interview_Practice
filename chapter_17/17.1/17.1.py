if __name__=="__main__":
    x = 5
    y = 1
    y ^= x
    x ^= y
    y ^= x
    print "Expect 5 - got {}; Expect 1 - got {}".format(y, x)
