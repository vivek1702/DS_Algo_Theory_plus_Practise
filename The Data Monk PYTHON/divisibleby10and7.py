# wap to give first 10 number which divsible by both 2 and 7:
count = 0
i = 1
while count <= 10:
    if i%2 == 0 and i%7 == 0:
        print(i, end=' ')
        count += 1
    i += 1