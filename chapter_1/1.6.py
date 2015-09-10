'''
CCC 1.6 Rotate an NXN matrix 90 degrees.
Can you do it in place?
'''

def manual_solution(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    manual_solution(a)
    # So lazy
    print 'Desired: [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]'
    print 'Actual: ',a
