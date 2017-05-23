
array1 = [1,2,-1,3,4,10,10,-10,-1]


def Longest_sum(array):
    if len(array) == 0:
        return 0

    currentSum = array[0]
    maxSum = array[0]

    for num in array[1:]:
        print(currentSum, num)
        currentSum = max(currentSum+num, num)

        maxSum = max(currentSum, maxSum)


    return maxSum

print(Longest_sum(array1))