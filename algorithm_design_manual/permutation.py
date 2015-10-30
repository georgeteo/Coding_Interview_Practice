def permutations(array):
    if len(array) == 0:
        yield []
    else:
        for i, letter in enumerate(array):
            splice = array[:i] + array[i+1:]
            for p in permutations(splice):
                # print p, letter
                yield [letter] + p

if __name__=="__main__":
    array=[1,2,3]
    for p in permutations(array):
        print p
