
def leaders(arr, n):
    maxi = arr[n-1]
    i = n-2
    ll = []
    ll.append(maxi)
    while i >= 0:
        if arr[i] > maxi:
            ll.append(arr[i])
            maxi = arr[i]
        i -= 1

    return ll[::-1]


# output = 17, 5, 2
#because 17 is greatest among all anf right to 17 is 5 greatest then 2 

arr = [16, 17, 3, 4, 5, 2]
n = len(arr)
print(leaders(arr, n))
