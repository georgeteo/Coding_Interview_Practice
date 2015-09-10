# CCC 1.8: Given a function isSubString(s1, s2), which determines if s1 is a 
# substring of s2, write a function isRotation(s1, s2) that determines whehter 
# s1 is a rotation of s2 calling isSubString only once. 
# An example of a rotation is: apples and plesap. 

def lol_solution(s1,s2):
    return isSubString(s1, s2+s2)
