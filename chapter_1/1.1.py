# CCC 1.1: Implement an algorithm to determine if a string 
# has all unique characters

import string
import sys

def main(s):
	alphabet = list(string.ascii_lowercase)
	for letter in s:
		try: 
			alphabet.remove(letter)
		except ValueError:
			return False
	return True

if __name__ == "__main__":	
	rv = main(sys.argv[1])
	if rv:
		print "True"
	else:
		print "False"
		
## George: O(n^2)
