'''
CCC 9.4: Write a method to return all subsets of a set.
'''

from Queue import Queue
import sys

def subset_generator(input_set):
    s = "".join(input_set)
    q = Queue()
    print ""
    for letter in s:
        q.put((letter, s.replace(letter, "")))
    while not q.empty():
        subset = q.get()
        yield subset[0]
        for letter in subset[1]:
            q.put((subset[0]+letter, subset[1].replace(letter, "")))

if __name__=="__main__":
    set_to_test = set(['a','b'])
    for subset in subset_generator(set_to_test):
        print subset
