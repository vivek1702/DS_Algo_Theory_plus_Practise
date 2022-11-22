

def pairSum(arr, n, num) :
    m = [0]*100
    for i in range(0,n):
        m[arr[i]] += 1

    twice_count = 0
    for i in range(0,n):
        twice_count += m[num -arr[i]]

        if (num - arr[i] == arr[i]):
            twice_count -= 1

    return (twice_count // 2)
        

arr = [1, 3, 6, 2, 5, 4, 3, 2, 4]
num = 7
n = len(arr)
print(pairSum(arr, n, num))

######################################################

#hashmap method o(n) and o(n)

# def pairSum(arr, n, num) :
#     dict_map = {}
#     count = 0
#     for i in range(n):
#         if num - arr[i] in dict_map:
#             count += dict_map[num - arr[i]]
#         if arr[i] in dict_map:
#             dict_map[arr[i]] += 1
#         else:
#             dict_map[arr[i]] = 1
#     return count