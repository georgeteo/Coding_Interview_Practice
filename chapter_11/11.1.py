'''
CCC 11.1: Given two sorted lists A and B, write a function that merges
B into A in sorted order
'''
def merge_sorted_list(A, B):
    '''
    Time Complexity: O(n^2) but slightly optimized
    Space Complexity: O(n)
    '''
    i = 0
    for b in B:
        for j, a in enumerate(A[i:]):
            if a < b:
                continue
            else:
                A.insert(j+i, b)
                i = j
                break
    return A

if __name__=="__main__":
    A = [1,3,5,7]
    B= [2,6]
    print merge_sorted_list(A,B)
