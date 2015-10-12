def reverse_string(string):
    string_list = list(string)
    mid = len(string_list)/2
    for i in range(mid):
        j = -1-i
        string_list[i],string_list[j] = string_list[j],string_list[i]
    return "".join(string_list)

if  __name__ == "__main__":
    even_test_string = "abcdef"
    print "Even Test string: ", even_test_string
    print "Swapped: ", reverse_string(even_test_string)

    odd_test_string = "abcdefg"
    print "Odd test string: ", odd_test_string
    print "Swapped: ", reverse_string(odd_test_string)
