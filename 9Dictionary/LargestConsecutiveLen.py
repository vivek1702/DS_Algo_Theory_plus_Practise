from sys import flags, stdin

def longestConsecutiveSubsequence(arr,n): 
    d = {}
    max = 0
    for i in arr:
        d[i] = 0

    for i in arr:
        s = i
        c = 0
        while s in d:
            d[s] = d[s]+1
            s += 1
            c += 1
        if c>max:
            si = i
            max = c

    return si,max+si-1


#approch that i like

# if len(array) == 0:
#             return 0
        
#         bestRange = []
#         longestLength = 0
#         nums = {}
#         for num in array:
#             nums[num] = True

#         for num in array:

#             if not nums[num]:
#                 continue

#             nums[num] = False
#             currentLength = 1
#             left = num-1
#             right = num+1

#             while left in nums:
#                 nums[left] = False
#                 currentLength+=1
#                 left -=1

#             while right in nums:
#                 nums[right] = False
#                 currentLength+=1
#                 right+=1

#             if currentLength > longestLength:
#                 longestLength = currentLength
#                 bestRange = [left+1,right-1]

#         return bestRange[1]-bestRange[0]+1
    


def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)