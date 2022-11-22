def findDuplicate(arr, n) :
    # arr.sort()
    # for i in range(0,n):
    #     if arr[i] == arr[i+1]:
    #         return arr[i]
    sumOfNminusTwoNaturalNumbers = 0
    for i in range(n - 1) :
        sumOfNminusTwoNaturalNumbers += i
    sumOfElements = 0
    for i in range(n) :
        sumOfElements += arr[i]
    return (sumOfElements - sumOfNminusTwoNaturalNumbers)


arr = [0, 2, 3, 4, 1, 4]
n = len(arr)
print(findDuplicate(arr, n))