from collections import Counter
n = int(input())
m = list(map(int, input().split()))
mc = Counter(m)
res = 0
a = int(input())
for i in range(0,a):
    x = input().split()
    if int(x[0]) in mc.keys():
        if mc[int(x[0])] > 0:
            res += int(x[1])
        mc[int(x[0])] -= 1

print(res)

