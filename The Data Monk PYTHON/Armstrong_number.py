def armstrong(n):
    
    a = 0
    while n > 0:
        num = n%10
        a += num ** 3
        n = n//10
    
    if a == n:
        return True
    else:
        return False


print(armstrong(153))

