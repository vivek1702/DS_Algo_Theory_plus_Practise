from sys import stdin
def maxfreq(arr):
    #Write your code here 
    d = {}
    for i in arr:
        d[i]=d.get(i,0)+1
            
    values=[i for i in d.values()]
    max_freq=max(values)
    for i in arr:
        if d[i]==max_freq:
            return i
#     for i in d:
#         if (max_count < d[i]):
#             res = i
#             max_count = d[i]
            
#     return res

    
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))

