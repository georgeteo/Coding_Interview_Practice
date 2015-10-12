# Remove Duplicates from string in place

### Solution

#### Method 1:

Make a hashset and remove subsequent duplicates.

Time Complexity: O(n)
Space Complexity: O(n)
Preserves Order

#### Method 2:

Sort string and remove duplicates.

Time Complexity: O(n)
Space Complexity: O(1) [depending on sorting algorithm]
Does not preserve order

### Issue

Python strings are immutable so convert to list (requires one pass). 
