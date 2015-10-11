def get_in_order_front_subarray(array):
    for i,j in enumerate(array[1:]):
        if array[i]<= j:
            continue
        else:
            break
    return i


if __name__=="__main__":
    array = [1,2,4,7,10, 11, 7, 12, 6, 7,16, 18, 19]
    front_i = get_in_order_front_subarray(array)
    middle_i = get_in_order_front_subarray(array[front_i+1:]) + front_i + 1
    print array[:front_i+1]
    print array[front_i+1:middle_i+1]
    print array[middle_i+1:]
