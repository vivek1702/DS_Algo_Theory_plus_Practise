# from collections import defaultdict
# n,m = map(int, input().split())
# d = defaultdict(list)
# for i in range(n):
#     a = input()
#     d[a] = i 

# for i in range(m):
#     b = input()
#     d[b] = i


from collections import defaultdict

n,m = list(map(int, input().split(" ")))
d = defaultdict(list)
for i in range(1,n+1):
    a = input()
    d[a].append(i)
    
for i in range(m):
    k = input()
    if k in d:
        print(d[k], sep= " ")
    else:
        print(-1)














