def reverse_string(string):
    cleaned = string.strip()
    split = cleaned.split()
    newArray = []

    for word in reversed(split):
        newArray.append(word)
    return newArray



string1 = "hello I am here to bang"
string2 = "hello     john  asdf    "
print(reverse_string(string1))
print(reverse_string(string2))


