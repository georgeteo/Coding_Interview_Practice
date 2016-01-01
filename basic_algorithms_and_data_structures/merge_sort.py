def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)/2
    sorted_left = merge_sort(arr[:mid])
