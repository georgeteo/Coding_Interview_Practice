def binary_search(arr, s, e, target):
    print (s,e)
    if s==e:
        return s
    mid = (e-s)/2
    if target <= arr[mid]:
        return binary_search(arr, s, mid, target)
    else:
        return binary_search(arr, mid+1, e, target)

if __name__=="__main__":
    arr = [-1,0,2,3,4]
    print binary_search(arr, 0, 4, 1)

