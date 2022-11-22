# def partitions(arr, start, end):
    # count = 0
    # pivot_val = arr[start]
    # for i in range(start, end):
    #     if arr[i] < pivot_val:
    #         count += 1
    # arr[start], arr[count] = arr[count], arr[start]
    # pivot_index = count

    # i = start
    # n = end

    # while i < n:
    #     if arr[i] < pivot_val:
    #         i += 1
    #     elif arr[n] > pivot_val:
    #         n -= 1
    #     else:
    #         arr[i], arr[n] = arr[n], arr[i]
    #         i += 1
    #         n -= 1

    # return pivot_index

def quickSort(arr, start, end):
    if start >= end:
        return

    pivot_index = partition(arr, start, end)
    quickSort(arr, start, pivot_index-1)
    quickSort(arr, pivot_index+1, end)

    return arr

def partition(arr, start, end):
         
    pivot_val = arr[end]
    i = start - 1
    
    for j in range(start, end):
        if arr[j] <= pivot_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]       
    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i+1


arr = [3, 6, 8, 2, 4, 5]
print(quickSort(arr, 0, len(arr)-1))
# print(partitions(arr, 0, len(arr)))