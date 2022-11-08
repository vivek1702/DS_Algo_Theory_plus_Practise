def sum_of_digit(n):
    if n==0:
        return 0
    sum = 0
    sum = sum + n%10
    n = n//10
    return sum + sum_of_digit(n)

n = int(input())
print(sum_of_digit(12357))