def sign(x):
    '''
    Return 1 if x is positive, 0 otherwise
    '''
    return ((x>>31) == 0)*1

def find_max(a,b):
    s = sign(a-b)
    f = 0 if s == 1 else 1
    return a * s + b * f

if __name__=="__main__":
    print "Expect 5 - got {}".format(find_max(5,-5))
