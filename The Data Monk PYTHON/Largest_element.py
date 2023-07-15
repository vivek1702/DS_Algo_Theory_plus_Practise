a=[1,5,7,3,4,9,18,222]

num1 = a[0]
for i in range(1, len(a)):
    if a[i] > num1:
        num1 = a[i]

print(num1)