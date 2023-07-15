

def concat_arr(n):
    a = [0] * len(n) * 2
    i = 0
    j = 0
    while j <= len(a)-1:
        a[j] = n[i]
        if i == len(n)-1:
            i = -1
        i += 1
        j += 1

    return a

nums = [1, 2, 1]
print(concat_arr(nums))

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]