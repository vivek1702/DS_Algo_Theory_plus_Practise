def subArraySum(arr, n, s): 
       #Write your code here
    left = 0
    sum = 0
    for right in range(n):
        sum = sum + arr[right]
        while sum > s:
            sum -= arr[left]
            left += 1
        if sum ==s and right>=left:
            return [left+1, right+1]
    return  [-1] 
        
a = [1, 2, 3, 7, 5]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = len(a)
c = 12
print(subArraySum(a, b, c))