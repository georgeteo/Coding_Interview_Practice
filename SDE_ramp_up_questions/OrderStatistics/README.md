# Order Statistics

A typical application of quick sort.

### Question

Find the kth biggest element in an array.

### Solution

Pick a pivot element and partition the array according to that element.
After the first split of quick sort, you know to look in the bottom m elements
if m > k or top n-m elements if m < k.

### Time Complexity

Since this is modified quick sort where you only have to look at half of the array,
in the average case, the expected running time is n + n/2 + n/4 + ... = O(n).
