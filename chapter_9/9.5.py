'''
CCC 9.5: Write a method to compute all permutations of a string of unique characters.
'''
from Queue import Queue

def permutation_generator(string):
    '''BFS Corecursion'''
    q = Queue()
    for letter in string:
        q.put((letter, string.replace(letter, "")))
    while not q.empty():
        substring = q.get()
        if len(substring[0]) > len(string):
            break
        if len(substring[0]) == len(string):
            yield substring[0]
        for letter in substring[1]:
            q.put((substring[0]+letter, substring[1].replace(letter, "")))

def print_permutations(string):
    for substring in permutation_generator(string):
        if len(substring) == len(string):
            print substring

if __name__=="__main__":
    print_permutations("abc")
