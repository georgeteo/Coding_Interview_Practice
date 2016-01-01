## Sorting/Searching

### Which sorting algorithm?

- Which sorting algorithm has minimum memory writes?
    - Selection sort
    - Cycle sort

### Common problems:

- Find minimum length unsorted subarray which makes array sorted
- Merge sort for linked list
- Sort an array where each element is off by k
    - Insertion sort with sliding window k
    - Heap sort with sliding window k
- Find k closest elements to a given value in sorted array
    - Binary search to find value
    - Linear search around that value
- Sort n numbers in range from 0 to n^2-1 in linear time
    - Radix sort
- Search an almost sorted array
    - Given an array where a[i] could be at a[i-1] or a[i+1], find the index of a given value
    - Do binary search but check equality at mid, mid-1, mid+1. If not, then recursively look in a[:mid - 1] or mid[mid + 2:].
- Sort in wave order: a[0] > a[1] < a[2] > a[3] ...
    - Sort, then flip adjacent elements
    - Or iterate through array and if current element is smaller than previous odd element, swap previous and current, and if current element is smaller than next odd element, swap next and current.
- Find kth smallest/largest element in unsorted array: Quick select
- Find pair in array whose sum is closest to x
    - Initialize start and end pointers
    - If a[s] + a[e] < sum: s++, else e--.


### Binary Search

#### Recursive

```Python
def recursive_binary_search(array, s, e, target):
    if s == e:
        return s
    mid = (e-s)/2
    if target <= array[mid]:
        return recursive_binary_search(array, s, mid, target)
    else:
        return recursive_binary_search(aray, mid+1, e, target)
```

#### Iterative
```Python
def iterative_binary_search(array, s, e, target):
    while s <= e:
        mid = (e-s)/2
        if target <= array[mid]:
            e = mid
        else:
            s = mid
    return s
```

### Selection Sort

```Python
def selection_sort(array):
    for i in range(n):
        min_index = i
        minimum_value = array[i]
        for j in range(i+1, n):
            if array[j] < minimum_value:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
```

### Bubble Sort

### Insertion Sort

### Merge Sort

#### TODO: Merge sort for linked list

### Heap Sort

### Quick Sort

Worst case occurs when array is sorted in same order or reverse order or all elements are the same.

#### Recursive

#### Iterative

#### TODO: Quick sort for singly and doubly linked lists

### Counting Sort

### Bucket Sort

### Shell Sort
