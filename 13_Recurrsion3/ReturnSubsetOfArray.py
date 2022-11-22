from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def subsetsUtil(A, subset, index):
    print(*subset)
    for i in range(index, len(A)):

        # include the A[i] in subset.
        subset.append(A[i])

        # move onto the next element.
        subsetsUtil(A, subset, i + 1)

        # exclude the A[i] from subset and
        # triggers backtracking.
        subset.pop(-1)
    return

# below function returns the subsets of vector A.


def subsets(A):
    global res
    subset = []

    # keeps track of current element in vector A
    index = 0
    subsetsUtil(A, subset, index)

# Driver Code


# find the subsets of below vector.
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    array = [int(element) for element in list(input().strip().split(" "))]
    return array, n

array, n = takeInput()
subsets(array)