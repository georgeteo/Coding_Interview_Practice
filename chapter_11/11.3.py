'''
CCC 11.3: Given a sorted array of n integers that have been rotated
write code to find an element in the array.
'''
def modified_binary_search(rotated_array, element):
    '''
    Modified Binary Search
    '''
    middle = len(rotated_array)/2
    middle_element = rotated_array[middle]
    left_slice = rotated_array[:middle]
    right_slice = rotated_array[middle+1:]
    print left_slice, right_slice
    if left_slice[0] <= middle_element:
        ''' Left slice is in order'''
        print "Left Slice"
        trigger = False
        in_order = left_slice
        other_slice = right_slice
    else:
        '''Right side in order'''
        print "Right Slice"
        trigger = True
        in_order = right_slice
        other_slice = left_slice
    if in_order[0] <= element and in_order[-1] >= element:
        print "Reg Binary Search"
        if trigger:
            return reg_binary_search(in_order, element) + middle
        return reg_binary_search(in_order, element)
    else:
        print "Modified Binary Search"
        if trigger is False:
            return modified_binary_search(other_slice, element) + middle
        return modified_binary_search(other_slice, element)


def reg_binary_search(array, element):
    '''
    Regular Binary Search
    '''
    middle = len(array)/2
    left_slice = array[:middle]
    right_slice = array[middle+1:]
    if element < array[middle]:
        return reg_binary_search(left_slice, element)
    elif array[middle] < element:
        return reg_binary_search(right_slice, element) + middle
    else:
        return middle

if __name__=="__main__":
    test_list = [4,5,7,9,1,2]
    print "Expected 4 - got ", modified_binary_search(test_list, 1)
