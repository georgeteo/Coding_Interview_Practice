from collections import defaultdict
import heapq

def rearrange_string(string):
    n = len(string)
    outstring = [0]*n
    h = defaultdict(int)
    for letter in string:
        h[letter] += 1
    h = [(-v,k) for k, v in h.items()]
    heapq.heapify(h)
    while len(h) != 0:
        offset = outstring.index(0)
        x = heapq.heappop(h)
        for i in range(-x[0]):
            if (offset + 2 * i) > n-1:
                return "False"
            outstring[offset + 2*i] = x[1]
    return "".join(outstring)

if __name__=="__main__":
    inputs = "aaabc"
    print inputs
    print rearrange_string(inputs)

    print "aa"
    print rearrange_string("aa")

    print "aaaabc"
    print rearrange_string("aaaabc")
