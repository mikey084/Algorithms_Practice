'''
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, 
or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
'''

def one_away(string1, string2):
    if string1.length == string2.length:
        return oneEditReplace(string1, string2)
    if string1.length + 1 == string2.length:
        return oneEditInsert(string1, string2)
    if string1.length - 1 == string2.length:
        return oneEditInsert(string1, string2)
    return False

def oneEditReplace(string1, string2):
    foundDifference = False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if foundDifference:
                return False
        foundDifference = True
    return True
