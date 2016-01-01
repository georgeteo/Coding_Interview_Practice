def reverse_string(string):
    stringlist = list(string)
    s = 0
    e = len(string) - 1
    while s <= e:
        stringlist[s], stringlist[e] = stringlist[e], stringlist[s]
        s += 1
        e -= 1
    return "".join(stringlist)

if __name__ == "__main__":
    string = "abcdef"
    print reverse_string(string)
