def count_Zeros(n):
    if n == 0:
        return 1
    if n < 10:
        return 0
    else:
        last_digit = n%10
        if last_digit == 0:
            return 1 + count_Zeros(n//10)

        return count_Zeros(n//10)
    

print(count_Zeros(109801))