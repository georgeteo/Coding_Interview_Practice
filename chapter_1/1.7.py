''' 
CCC 1.7: Given an NXN matrix, if an element = 0, make that row and col 0
'''

def simple_solution(a):
    row_zeroes = set()
    column_zeroes = set()
    n = len(a)
    for i in xrange(n):
        for j in xrange(n):
            if a[i][j] == 0:
                row_zeroes.add(i)
                column_zeroes.add(j)
            
    for i in row_zeroes:
        a[i] = [0]*n

    for j in column_zeroes:
        for i in xrange(n):
            a[i][j] = 0
