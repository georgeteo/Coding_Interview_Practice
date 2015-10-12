def rotate_clockwise(matrix):
    return zip(*matrix[::-1])

def rotate_counterclockwise(matrix):
    return zip(*matrix)[::-1]

def print_matrix(matrix):
    for row in matrix:
        print row

if __name__=="__main__":
    test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print "Test Matrix: "
    print_matrix(test_matrix)
    print "Rotate 90 degrees right: "
    print_matrix(rotate_clockwise(test_matrix))
    print "Rotate 90 degrees left: "
    print_matrix(rotate_counterclockwise(test_matrix))
