# Given two strings, check whether they are permutations of each other.

from collections import defaultdict
def is_permutation_1(s, t):
    '''
    O(n)
    '''
    letter_cnt = defaultdict(int)
    for letter in s:
        letter_cnt[letter] += 1
    for letter in t:
        letter_cnt[letter] -= 1
        if letter_cnt[letter] < 0:
            return False
    return True     

def is_permutation_2(s,t):
    '''
    O (n logn)
    '''
    return sorted(s) == sorted(t)
    
if __name__ == "__main__":
    print "Test Suite"
    print ""

    print "True Test"
    s1 = "abbc"
    t1 = "babc"
    print "Count Letters Method: %r"%is_permutation_1(s1, t1)
    print "Sort Letters Method: %r"%is_permutation_2(s1, t1)

    print ""
    print "False Test"
    s2 = "abbc"
    t2 = "abcd"
    print "Count Letters Method: %r"%is_permutation_1(s2, t2)
    print "Sort Letters Method: %r"%is_permutation_2(s2, t2)
    
