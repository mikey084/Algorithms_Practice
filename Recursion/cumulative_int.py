#Given an integer, create a function which returns the sum of all the individual
#Digits in that integer. For example: if n = 4321, return 4+3+2+1

array1 = [1,0,0,2,5,2,0,5]

def change_zeros(array):
    newArray = []
    for num in array:
        if num == 0:
            newArray.append(array[num:num+1])
    print(newArray)
    return array + newArray

print(change_zeros(array1))