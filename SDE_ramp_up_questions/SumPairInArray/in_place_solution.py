def sorted_in_place_solution(array, s):
    array.sort()
    i = 0
    j = len(array)-1
    while i < j:
        possible_sum = array[i] + array[j]
        if possible_sum == s:
            return array[i], array[j]
        elif possible_sum < s:
            i += 1
        else:
            j -= 1
    return False

if __name__=="__main__":
    a = [1,3,6,12,64,5]
    print "Expected (6,5) - got ", sorted_in_place_solution(a, 11)
    print "Expected False - got ", sorted_in_place_solution(a,-10)
