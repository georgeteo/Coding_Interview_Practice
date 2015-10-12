def hash_solution(array, s):
    hashset = set()
    for entry in array:
        hashset.add(entry)
    for entry in list(hashset):
        if s - entry in hashset:
            return entry, s-entry
    return False

if __name__=="__main__":
    a = [1,3,6,12,64,5]
    print "Expected (6,5) - got ", hash_solution(a, 11)
    print "Expected False - got ", hash_solution(a,-10)
