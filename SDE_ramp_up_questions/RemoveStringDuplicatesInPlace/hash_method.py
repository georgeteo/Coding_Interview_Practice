def hash_method(string):
    string_list = list(string)
    found_letters = set()
    i = 0
    while i < len(string_list):
        letter = string_list[i]
        if letter in found_letters:
            del string_list[i]
        else:
            found_letters.add(letter)
            i+=1
    return "".join(string_list)


if __name__=="__main__":
    test_string = "bbcacca"
    print "Test String ", test_string
    print "Duplicates removed ", hash_method(test_string)
