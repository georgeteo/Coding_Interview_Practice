'''
CCC 11.5: Given a sorted array of strings which is interspersed
with an arbitrary number of empty strings, write a method to find
the location of a given string.
'''

def find_location(array, x):
    '''
    Modified Binary Search
    '''
    middle = len(array)/2
    middle_x = array[middle]
    if middle_x == "":
        ''' Find closest non "" letter '''
        for i in xrange(1, middle+1):
            if array[middle-i] != "":
                middle = middle -i
                middle_x = array[middle]
                break
            elif array[middle+i] != "":
                middle = middle + i
                middle_x = array[middle]
                break
        ''' Could throw error if makes it to here without changing middle_x'''
    ''' Now middle_x is not "", so do regular binary search'''
    if x < middle_x:
        return find_location(array[:middle], x)
    elif x > middle_x:
        return find_location(array[middle+1:], x) + middle +1
    else:
        return middle

if __name__ == "__main__":
    test_list = ["a", "", "", "b", "", "c"]
    print "Expect 0 - got ", find_location(test_list, "a")
    print "Expect 3 - got ", find_location(test_list, "b")
    print "Expect 5 - got ", find_location(test_list, "c")
