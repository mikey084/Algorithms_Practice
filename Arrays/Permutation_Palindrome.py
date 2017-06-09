'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco
cat'; "atc o
eta·; etc.)
'''

import string

def permutation_palindrome(str):
    d = dict.fromkeys(string.ascii_lowercase, False)
    count = 0
    print(d)
    #builds dict keys for each lowercase letter and assigns False as the value
    for char in str:
        if ord(char) > 97 and ord(char) < 123:
            d[char] = not d[char]
    for key in d:
        if d[key] == True:
            count += 1
            if count > 1:
                return False

    return True

print(permutation_palindrome('aa bb rz cc dd'))


