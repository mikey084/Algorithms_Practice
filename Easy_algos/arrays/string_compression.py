#given AAAABBBBBBCCCDDDDDDD
#return
# A4B6C3D7

def string_compression(string):
    r = ""
    length = len(string)

    if length ==0:
        return ""
    if length == 1:
        return string + "1"

    count = 1
    index = 1

    while index < length:
        if string[index] == string[index-1]:
            count += 1
        else:
            r = r + string[index-1] + str(count)
            count = 1
        index += 1

    r = r + string[index-1] + str(count)
    return r

print(string_compression("AAAAAABBBBCCCDDDDDDPPPPPPPPPPP"))


