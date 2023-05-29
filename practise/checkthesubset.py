number_of_operations = int(input())
s = ""
for i in range(0, number_of_operations):
    n = int(input())
    s1 = set(map(int, input().split()))
    m = int(input())
    s2 = set(map(int, input().split()))
    if s1.issubset(s2):
        s += "True\n"
    else:
        s += "False\n"

print(s)

