ll = [5, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3]
d = {}
for i in ll:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

a = 0
b = 0
for i, j in d.items():
    if j > a:
        a = j
        b = i 

print(b, a)