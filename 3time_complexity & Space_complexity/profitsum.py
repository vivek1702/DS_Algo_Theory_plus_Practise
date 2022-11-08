def maximumProfit(arr):
	#Implement Your Function here
    arr.sort()
    n = len(arr)
    maxVal = arr[0] * n
    result = 0
    for i in range(1, n):
        if (arr[i] * n-i) > maxVal:
            maxVal = arr[i] * n-i
            result = arr[i]
    return result
    

arr = [34, 78, 9, 0, 15, 67]
print(maximumProfit(arr))

#wrong answer to revisit and do it again