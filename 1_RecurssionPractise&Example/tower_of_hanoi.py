def towerofhanoi(n, a, b, c):
    if n == 1:
        print(a,c)
        return
    towerofhanoi(n-1, a, c, b)
    print(a,c)
    towerofhanoi(n-1, b, a, c)


print(towerofhanoi(2, "a","b","c"))