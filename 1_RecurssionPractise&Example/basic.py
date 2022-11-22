def power(n, e):
    if e == 0:
        return 1
    elif e == 1:
        return n
    else:
        return (n*power(n, e-1))
        
n = 2
p = 3
print(power(n, p))