def rotate(arr, n, d):
    temp = []
    for i in range(0, d):
        temp.append(arr[i])

    
    for i in range(0,n):
        arr[i] = arr[i+d]

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
print(rotate(arr, n, d))
