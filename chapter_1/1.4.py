# CCC 1.4: Given a string, replace spaces with %20.

import re

def regex_solution(s):
    '''
    Complexity = ?

    Extension: how to get %20 for one set of arbitrarily many spaces?
    '''
    return re.sub(r"\s", "%20", s)

if __name__ == "__main__":
    print "Test Suite"
    test_string = "a b  c"
    print "Input String: %s"%test_string
    print "Processed String: %s"%regex_solution(test_string)
