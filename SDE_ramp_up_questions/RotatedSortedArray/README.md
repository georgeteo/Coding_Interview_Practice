# Rotated Sorted Array

### Question

Find an element in a rotated sorted array.

### Solution

Modified binary search

Find the middle of the array.

Compare the left most element of the left array and the right most element of the
right array with the middle element.

One of them is not correct.

Use that to decide which direction to continue the binary search.
