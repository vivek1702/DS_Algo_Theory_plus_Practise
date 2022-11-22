# Longest increasing subsequence
from sys import stdin

def lis(arr): 
    # Write your code here
    s = [None for i in range(n)]
    s[0] = 1
    ans = 1
    for i in range(1, n):
        max = 1
        for j in range(i-1, -1, -1):
            if(arr[j]<arr[i]):
                op = s[j] + 1

                if (op>max):
                    max = op

        s[i] = max
        if(max>ans):
            ans = max

    return ans
        

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    

arr,n=takeInput()
print(lis(arr))