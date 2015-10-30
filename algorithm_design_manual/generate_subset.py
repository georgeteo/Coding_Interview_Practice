# def generate_subset(subset_so_far, letters_to_pick_from):
#     print subset_so_far
#     n = len(letters_to_pick_from)
#     for i, letter in enumerate(letters_to_pick_from):
#         subset_so_far.append(letter)
#         new_letters_to_pick_from = letters_to_pick_from[:i]
#         if i < n-1:
#              new_letters_to_pick_from += letters_to_pick_from[i+1:]
#         generate_subset(subset_so_far, new_letters_to_pick_from)
#         subset_so_far.pop()

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            # print "Item: ", item 
            yield [seq[0]]+item
            yield item

if __name__=="__main__":
    array=[1,2,3]
    # generate_subset([], array)
    for p in powerset(array):
        print p
