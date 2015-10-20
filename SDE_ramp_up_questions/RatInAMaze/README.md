# Rat in a Maze

### Solution

**Backtracking**

Initialize a maze matrix and a solution matrix.

If destination is reached, print solution matrix.

Else,

1. Mark current cell 1 (to indicate path).
2. Recursively check right path.
3. Recursively check bottom path.
4. If both false, mark cell 0 and return false.
