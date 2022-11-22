def find_steps(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return find_steps(n-3) + find_steps(n-2) + find_steps(n-1)

n = int(input())
print(find_steps(n))