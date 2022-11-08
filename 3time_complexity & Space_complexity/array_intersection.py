from more_itertools import partition


def intersection(arr1, arr2, n, m):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    res = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            j += 1
        if arr1[i] > arr2[j]:
            i += 1
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1

    return res

arr1 = [2, 6, 8, 5, 4, 3]
arr2 = [2, 3, 4, 7]
n = len(arr1)-1
m = len(arr2)-1
print(intersection(arr1, arr2, n, m))