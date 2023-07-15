# 1 
# 2 3
# 4 5 6
# so on

n = 0
for i in range(1, 5):
    for j in range(i):
        n = n + 1
        print(n,end=' ')
    print()
