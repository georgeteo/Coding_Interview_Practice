def transpose(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for row in range(num_rows):
        for col in range(row, num_cols):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

def row_swap(matrix):
    num_cols = len(matrix[0])
    mid = num_cols/2
    for row in matrix:
        for i in range(mid):
            j = i-1
            row[i], row[j] = row[j], row[i]

def rotate_clockwise(matrix):
    transpose(matrix)
    row_swap(matrix)

def col_swap(matrix):
    num_rows = len(matrix)
    mid = num_rows/2
    for col_num in range(len(matrix[0])):
        for i in range(mid):
            j = num_rows - 1 - i
            matrix[i][col_num], matrix[j][col_num] = matrix[j][col_num], matrix[i][col_num]
def rotate_counterclockwise(matrix):
    transpose(matrix)
    col_swap(matrix)

def print_matrix(matrix):
    for row in matrix:
        print row

if __name__=="__main__":
    test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print "Test Matrix: "
    print_matrix(test_matrix)
    print "Rotate Clockwise:"
    rotate_clockwise(test_matrix)
    print_matrix(test_matrix)

    test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print ""
    print "Reset Test Matrix: "
    print_matrix(test_matrix)
    print "Rotate Counter Clockwise"
    rotate_counterclockwise(test_matrix)
    print_matrix(test_matrix)
