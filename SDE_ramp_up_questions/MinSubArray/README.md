# Find Minimum SubArray

1. Search from left->right, set start_index as first time i+1 < i.
2. Search from right->left, set end_index as first time j-1 > j.
3. Find min, max of A[start...end]
4. In A[...start], reset start_index if there is a place that has value > min.
5. In A[end...], reset end_index if there is a place that has value < max.
