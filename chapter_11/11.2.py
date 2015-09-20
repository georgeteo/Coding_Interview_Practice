'''
CCC 11.2: Write a method to sort an array of strings so that
all anagrams are next to each other.
'''
from collections import defaultdict

class anagram_hash:
    def __init__(self):
        self.dictionary = defaultdict(list)

    def hash_word(self, word):
        '''
        Time Complexity: O(nlogn) # Merge sort
        Space Complexity: O(n)
        '''
        key = ''.join(sorted(list(word)))
        self.dictionary[key].append(word)

    def to_list(self):
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        master_list = []
        for sublist in self.dictionary.values():
            master_list = master_list + sublist
        return master_list

if __name__=="__main__":
    test_list = ["abc", "cba", "bca", "def", "cde"]
    AH = anagram_hash()
    for word in test_list:
        AH.hash_word(word)
    print AH.to_list()
