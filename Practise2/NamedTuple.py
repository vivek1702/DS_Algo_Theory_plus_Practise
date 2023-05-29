from collections import namedtuple

n = int(input())
student = namedtuple('student', input())
total = 0
for i in range(0,n):
    s = student(*input().split())
    total += int(s.Marks)

print("{0:.2f}".format(total/n))

