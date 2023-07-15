list_1 = [(1,2,3),(3,4,5),(2,3),(7,8,9)]
k = 2
res = [list_1[i] for i in range(len(list_1)) if i != k]
print(res)
