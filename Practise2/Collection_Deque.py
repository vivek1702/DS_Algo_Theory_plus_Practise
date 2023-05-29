from collections import deque
d = deque()
n = int(input())
for i in range(0,n):
    a = input().split()
    if a[0] == 'append':
        d.append(a[1])
    elif a[0] == 'appendleft':
        d.append(a[1])
    elif a[0] == 'pop':
        d.pop()
    elif a[0] == 'popleft':
        d.popleft()
    
print(*d)