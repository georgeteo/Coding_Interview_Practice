# CCC 1.5: Given a string, compress it into a sparse vector. 
# If no compression, return the regular string
# e.g., aabbaaac = a2b2a3c

def compress_string(s):
    '''
    O(n)
    '''
    compressed_string = [s[0], 1]
    compressed = False
    for letter in s[1:]:
        if letter == compressed_string[-2]:
            compressed_string[-1] += 1
            compressed = True 
        else:
            compressed_string = compressed_string + [letter, 1]
    if compressed:
        compressed_string = [str(s) for s in compressed_string] #Dumb, better way? 
        return "".join(compressed_string)
    else:
        return s

if __name__ == "__main__":
    print "Tests\n"
    s = "aabbaaac"
    desired_s = "a2b2a3c1"
    output_s = compress_string(s)
    print "Input string: %s"%s
    print "Desired string: %s"%desired_s
    print "Returned string: %s"%output_s


    print ""
    t = "abcde" 
    print "Input string: %s"%t
    print "Desired string: %s"%t
    print "Output string: %s"%compress_string(t)
