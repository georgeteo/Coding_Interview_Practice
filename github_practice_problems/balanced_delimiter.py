def correct_closer(last_char, char):
    if char == ")" and last_char == "(":
        return True
    if char == "]" and last_char == "[":
        return True
    if char == "}" and last_char == "{":
        return True
    return False

def is_balanced(string):
    '''Stack based solution'''
    s = []
    for char in string:
        if char == "(" or char == "[" or char == "{":
            s.append(char)
        else:
            if not correct_closer(s[-1], char):
                return False
    return True

'''
Is there a recursive solution?

Only if there are two branches: encompassing by removing or split by removing.
'''
