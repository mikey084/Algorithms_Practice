import collections
array1 = [1,2,3,4,5,6,7]
array2 = [1,3,2,5,6,4]

def check_two_arrays(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]



print(check_two_arrays(array1, array2))


def check_two_arrays2(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] +=1

    for num in arr1:
        if d[num] == 0:
            return num
    else:
        d[num] -= 1

print(check_two_arrays2(array1,array2))