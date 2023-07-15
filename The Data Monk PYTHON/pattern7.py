#1
#0 1
#1 0 1
#0 1 0 1

for i in range(1, 6):
    for j in reversed(range(i)):
        if j%2 ==0:
            print(1, end='')
        else:
            print(0, end='')
    print()