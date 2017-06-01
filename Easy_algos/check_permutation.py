'''
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
'''


def permutation(string1, string2):
    split1 = list(string1)
    split2 = list(string2)

    unique1 = set()
    unique2 = set()
    print(split1, split2)
    for x in string1:
        unique1.add(x)

    for n in string2:
        unique2.add(n)

    if unique1 == unique2:
        return True

    return False



s1 = "asdfg"
s2 = "gfdsa"

print(permutation(s1, s2))
