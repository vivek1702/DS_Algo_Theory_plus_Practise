
def arrayEquilibriumIndex(arr, n):
    i = 0
    total_sum = 0
    while i <= n:
        total_sum += arr[i]
        i += 1
    
    left_sum = 0
    right_sum = 0
    indexx = 0
    l = []
    while indexx <= n:
        right_sum = total_sum - left_sum - arr[indexx]
        if left_sum == right_sum:
            l.append(indexx)
            left_sum += arr[indexx]
            indexx += 1
        else:
            left_sum += arr[indexx]
            indexx += 1

    if len(l) == 0:
        return -1
    else:
        return l

arr = [1, 4, 6]
n = len(arr) - 1
print(arrayEquilibriumIndex(arr, n))