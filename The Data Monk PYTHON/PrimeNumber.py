
def prime_number(n):

    for i in range(2, int(n/2)+1):
        if n%i == 0:
            return False
    return True

print(prime_number(12))