def remove_duplicates_via_sorting(string):
    string_list = list(string)
    string_list.sort()
    i = 0
    for letter in string_list[1:]:
        if letter == string_list[i]:
            del string_list[i+1]
            i -= 1
        i += 1
    return "".join(string_list)

if __name__=="__main__":
    test_string = "bbcacca"
    print "Test String ", test_string
    print "Duplicates removed ", remove_duplicates_via_sorting(test_string)
