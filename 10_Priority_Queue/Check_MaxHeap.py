#Given an array of integers,
#  check whether it represents max-heap or not.
#  Return true if the given array represents max-heap, else return false.

def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    n = len(lst)
    for i in range(int((n - 2) / 2) + 1):
         
        # If left child is greater,
        # return false
        if lst[2 * i + 1] > lst[i]:
                return False
 
        # If right child is greater,
        # return false
        if (2 * i + 2 < n and
            lst[2 * i + 2] > lst[i]):
                return False
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')