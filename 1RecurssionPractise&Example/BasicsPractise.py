def sum_n(n):
    if n == 0:
        return 0
    smalloutput = sum_n(n-1)
    output = smalloutput + n
    return output

    
n = int(input())
print(sum_n(5))


# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     first_num = fib(n-1)
#     second_num = fib(n-2)
#     output = first_num + second_num
#     return output

# n = 5
# print(fib(n))

def fun(n):
    if(n == 5):
        return n
    else:
        return 2 * fun(n+1)

print(fun(3))


# def sumArray(arr):   
#     l = len(arr)
#     if l == 0:
#         return None
#     if l == 1:
#         return arr[0]
#     else:
#     	return arr[0] + sumArray(arr[1:])

# arr = [3, 9, 7]
# print(sumArray(arr))


# def checkNumber(arr, x):
#     # Please add your code here
#     if len(arr) == 0:
#         return False
#     if arr[0] == x:
#         return True
    
#     return checkNumber(arr[1:], x)


# # arr = [34, 57, 82, 41, 65, 35, 82, 27, 36, 12, 6, 40, 66, 99, 25, 29, 
# # 22, 25, 12, 24, 65, 15, 5, 43, 28, 33, 76, 32, 13, 95, 22, 84, 71, 23, 28, 7, 65, 94, 18, 47, 9, 42, 61, 73]
# arr = [1, 3, 61, 5]
# x = 61

# print(checkNumber(arr, x))


# def ishort(arr, x):
#     l = len(arr)
#     if x == l-1 or l == 0:
#         return True
#     if arr[x] > arr[x+1]:
#         return False
     
#     return ishort(arr, x+1)

# arr = [2, 4, 5, 7, 11, 50, 12]
# x = 0
# print(ishort(arr,x))

# def firstIndex(arr, x):
#     # Please add your code here
#     if len(arr) == 0:
#         return -1
#     elif arr[0] == x:
#         return 0
    
#     rv = firstIndex(arr[1:], x)
#     if rv < 0:
#         return rv
#     return rv + 1

# arr = [1, 2, 4, 5, 6, 7, 9, 9, 11]
# x = 9
# print(firstIndex(arr,x))


# def LastIndex(arr, x):
#     if len(arr) == 0:
#         return -1 
    
#     rv = LastIndex(arr[1:], x)
#     if rv != -1:
#         return rv + 1
#     else:
#         if arr[0] == x:
#             return 0
#         else:
#             return -1

# arr = [1, 2, 4, 5, 6, 7, 9, 9, 11]
# x = 9
# print(LastIndex(arr,x))















