def substring(string, sub):
    if len(sub) == 1:
        if sub == string[0]:
            return True
        else:
            return False
    if not string:
        return False
    else:
        rv1 = False
        rv2 = False
        if sub[0] == string[0]:
            rv1 = substring(string[1:], sub[1:])
        rv2 = substring(string[1:], sub)
        return rv1 or rv2

if __name__=="__main__":
    string = "abcdbce"
    print substring(string, "ab")
    print substring(string, "bce")
    print substring(string, "dc")
