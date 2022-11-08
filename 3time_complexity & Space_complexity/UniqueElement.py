def findUnique(arr, n):
    # lv = 0
    # while lv < n:
    #     mid = (lv + n) // 2
    #     if (mid % 2 == 1 and arr[mid-1] == arr[mid]) or (mid % 2 == 0 and arr[mid]== arr[mid + 1]):
    #         lv = mid + 1
    #     else:
    #         n = mid
    # return arr[lv]

############################################################

    # arr.sort()
    # for c in arr:
    #     if arr.count(c) == 1:
    #         return c

    #o(n^2) s= o(1)


arr = [2, 3, 1, 6, 3, 6, 2, 7]
n = len(arr)-1
print(findUnique(arr, n))

#this can be ask in interview and time complexity would be o(nlogn)

# EXPLANATION:-
# Suppose array is [1, 1, 2, 2, 3, 3, 4, 5, 5]
# we can observe that for each pair, 
# first element takes even position and second element takes odd position
# for example, 1 is appeared as a pair,
# so it takes 0 and 1 positions. similarly for all the pairs also.

# this pattern will be missed when single element is appeared in the array.

# From these points, we can implement algorithm.
# 1. Take left and right pointers . 
#     left points to start of list. right points to end of the list.
# 2. find mid.
#     if mid is even, then it's duplicate should be in next index.
# 	or if mid is odd, then it's duplicate  should be in previous index.
# 	check these two conditions, 
# 	if any of the conditions is satisfied,
# 	then pattern is not missed, 
# 	so check in next half of the array. i.e, left = mid + 1
# 	if condition is not satisfied, then the pattern is missed.
# 	so, single number must be before mid.
# 	so, update end to mid.
# 3. At last return the nums[left]

# Time: -  O(logN)
# space:-  O(1)