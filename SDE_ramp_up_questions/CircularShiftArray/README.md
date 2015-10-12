# Rotate a list by k

### Method 1

Use another array to store the rotation.

### Method 2:

Rotate by one offset multiple times.

Time Complexity: O(n*k)

### Method 3:

Compute GCD(n,k).

Split array into chunks of the gcd and move things by the gcd hops.

Time Complexity: O(n)

### Method 4:

Split array into two parts: A[1...k-1]B[k...n].

- Reverse A
- Reverse B
- Reverse back (ArBr)
