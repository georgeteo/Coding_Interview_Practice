# Find a pair in an array that sums to a desired number

### Solution:

Method 1:
Store all elements in the array in a set.
Iterate back through the set, checking if sum - x in set.
If yes, return.

Method 2:
Sort array.
Start with i = 0, j = n-1,
Increment or decrement i or j appropriately.
