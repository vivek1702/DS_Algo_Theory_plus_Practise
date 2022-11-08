
def PredictTheWinner(nums):
    lv = 0
    rv = len(nums)-1
    first_val = 0
    second_val = 0
    if nums == 0:
        return 

    helper1(nums, lv, rv, first_val)
    helper2(nums, lv, rv, second_val)

    if first_val >= second_val:
        return True

    else:
        return False


def helper1(nums, lv, rv, first_val):

    if nums[lv] > nums[rv]:
        first_val += nums[lv]
        lv += 1
    elif nums[rv] > nums[lv]:
        first_val += nums[lv]
        rv -= 1
    return first_val


def helper2(nums, lv, rv, second_val):

    if nums[lv] > nums[rv]:
        second_val += nums[lv]
        lv += 1
    elif nums[rv] > nums[lv]:
        second_val += nums[lv]
        rv -= 1
    return second_val


        
print(PredictTheWinner(nums=[1, 5, 2]))