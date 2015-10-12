def max_sub_array(array):
    max_ending_here = max_so_far = array[0]
    start = 0
    end = 0
    for i, x in enumerate(array[1:], start=1):
        max_ending_here = max(x, max_ending_here+x)
        if max_ending_here == x:
            start = i
        max_so_far = max(max_ending_here, max_so_far)
        if max_so_far == max_ending_here:
            end = i
    return max_so_far, start, end

if __name__=="__main__":
    test = [-2,1,-3,4,-1, 2,1,-5,4]
    print "Expect (6, 3, 6) - got ", max_sub_array(test)
