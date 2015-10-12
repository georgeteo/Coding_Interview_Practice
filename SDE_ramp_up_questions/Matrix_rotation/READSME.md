# Matrix Rotation

### Question

Given a n x n matrix represented by a list of lists `[[1,2,3],[4,5,6],[7,8,9]]` ,
rotate the matrix by 90 degrees to the left, right and 180 degrees.

### Solution

90 degree to the right:
    1. Transpose
    2. Reverse rows

90 degrees to the left:
    1. Transpose
    2. Reverse columns

180 degrees:
    1. Reverse rows and columns

### Python shortcut:

```Python
rotate_clockwise = zip(*matrix[::-1])
rotate_counterclockwise = zip(*matrix)[::-1]
```
