# CCC 1.1: Implement an algorithm to determine if a string 
# has all unique characters

import string
import sys

def wrong_solution(s):
    """
    Time:   O(n)
    Space:  Unclear

    """
    return len(s) == len(s)


def set_solution(s):
    """
    Time:   O(n)
    Space:  Unclear

    """
    return len(set(s)) == len(s)


def sort_solution(s):
    """
    Time:   O(nlogn)
    Space:  O(n)
    """
    sorted_s = sorted(s)
    for i in xrange(len(sorted_s)-1):
        if sorted_s[i] == sorted_s[i+1]:
            return False

    return True


def test(sol_function):
    assert sol_function("abcd1234") == True
    assert sol_function("abcd1234a") == False
    assert sol_function("abcd1234A") == True

    print "All tests passed"


SOLUTIONS = {"wrong": wrong_solution,
             "set": set_solution,
             "sort": sort_solution
             }


def main(solution_name):
    if solution_name in SOLUTIONS:
        solution = SOLUTIONS[solution_name]
        return test(solution)

    else:
        print "Unknown solution"
        return False


if __name__ == "__main__":  
    main(sys.argv[1])
