import math

n = int(input("Enter a number = "))
def sq(n):
    s = int(math.sqrt(n))
    return s*s == n
print("The status of number = " , sq(n))
