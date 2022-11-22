def mergeSort(arr, start, end):
    if len(arr) == 0 or len(arr) == 1:
        return

    mid = len(arr)//2

    arr1 = arr[:mid]
    arr2 = arr[mid:]

    mergeSort(arr1, start, mid)
    mergeSort(arr2, mid, end)

    merge2(arr1, arr2, arr)

    return arr


def merge2(arr1, arr2, arr):

    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
            k += 1

        else:       
            arr[k] = arr2[j]
            j += 1
            k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1

           
arr = [2, 6, 8, 5, 4, 3]
print(mergeSort(arr, 0, len(arr)))