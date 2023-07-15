# fabonacci series 0,1,1,2,3,5,8,13,21
n = int(input())

num1 = 0
num2 = 1
next_num = 0
count = 1
while count <= n:
    print(next_num, end=', ')
    count += 1
    num1 = num2
    num2 = next_num
    next_num = num1 + num2


