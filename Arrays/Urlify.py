'''
URLify: Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string. 
(Note: if implementing in Java, please use a character array so that you can perform this operation in place.)

EXAMPLE
Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"
'''


def urlify(string):
    res = ''
    str = string.strip()

    for char in str:
        if char == ' ':
            res += '%20'

        else:
            res += char

    return res


string1 = "mr john smith"
print(urlify(string1))