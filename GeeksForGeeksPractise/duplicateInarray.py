def duplicates(arr, n): 
    	# code here
    ll = []
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                ll.append(arr[i])
                
    if len(ll) > 0:
        return ll
    else:
        return -1
    
arr = [2,3,1,2,3,1,11,12,11,14]
n = len(arr)
print(duplicates(arr, n))