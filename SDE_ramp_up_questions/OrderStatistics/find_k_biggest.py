def pivot(array):
    pivot = array[0]
    not_complete = True
    i = 1
    j = len(array) - 1
    while not_complete:
        while i < len(array) and not_complete:
            if array[i] > pivot:
                swap_bottom = True
                break
            if i == len(array)-1:
                not_complete = False
            i += 1

        while j > 0 and not_complete:
            if array[j] < pivot:
                swap_top = True
                break
            if j == 1:
                not_complete=False
            j -= 1

        if j < i:
            array[j], array[0] = array[0], array[j]
            not_complete = False
            break

        if swap_bottom and swap_top:
            array[i], array[j] = array[j], array[i]
            swap_bottom = False
            swap_top = False

    return j, pivot

def find_k_biggest(index, array):
    pivot_index, pivot_val = pivot(array)
    if pivot_index == index:
        return pivot_val
    if pivot_index < index:
        return find_k_biggest(index - pivot_index-1, array[pivot_index + 1 :])
    else:
        return find_k_biggest(index, array[:pivot_index])




if __name__=="__main__":
    array = [5,10,1,2,3,6,7,4,8,9]
    print "Input Array ", array
    print "Pivot index and value ", pivot(array)
    print "Pivoted Array ", array

    print ""
    array = [5,10,1,2,3,6,7,4,8,9]
    print "Input Array ", array
    print "Expected 8 - got ", find_k_biggest(7, array)
