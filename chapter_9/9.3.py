'''
CCC 9.3.: A magic index in an array A[0...n-1] is defined to be an index such
that A[i] = i. Given a sorted array of distinct integers, write a method to
find a magic index if one exists.

What if values are not distinct
'''

def find_magic_index(array):
    ''' Modified Binary Search'''
    def binary_search(i, j):
        mid = len(array[i:j])/2
        if array[mid] == mid:
            return mid
        if len(array) == 1 and array[mid] != mid:
            return False
        if array[mid] < mid:
            '''Look on right half'''
            return binary_search(mid+1, j)
        else:
            return binary_search(i, mid)
    return binary_search(0, len(array))

if __name__=="__main__":
    test_array = [-1, 1, 4, 5, 7]
    print "Expected 1 - got", find_magic_index(test_array)
