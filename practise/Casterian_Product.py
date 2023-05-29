
from itertools import product


n = list(map(int, input().split()))
m = list(map(int, input().split()))

x = [(i,j) for i in n for j in m]
print(*x, sep='')