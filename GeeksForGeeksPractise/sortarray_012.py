

def sort012(arr, n):
    low = 0
    mid = 0
    high = n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
            mid += 1
        
        else:
            mid += 1

    return arr

n = int(input())
# arr = []
# for i in range(n):
#     a = int(input())
#     arr.append(a)

arr = list(map(int, input().split()))

print(sort012(arr, n))