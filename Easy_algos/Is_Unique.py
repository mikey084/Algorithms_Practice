'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

def Is_Unique(string):
    length = len(string)
    split = set(string)

    if len(split) == length:
        return True

    return False


string = "asdfggg"
string1 = "asdfg"
string2 = "12231"

print(Is_Unique(string))
print(Is_Unique(string1))
print(Is_Unique(string2))