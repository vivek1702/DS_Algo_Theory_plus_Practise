n = int(input())
m = list(map(int, input().split()))
print(n)
print(m)

dictn = {}
for i in m:
    if i in dictn:
        dictn[i] += 1
    else:
        dictn[i] = 1

for i, j in dictn.items():
    if j == 1:
        print(i)

#here given a num and another list contains a group 