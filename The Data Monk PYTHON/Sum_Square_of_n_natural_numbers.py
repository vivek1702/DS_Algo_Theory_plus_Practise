# def natural_num_sum(n):
#     if n == 0:
#         return
    
#     a = n + (n*n)
#     return a


# x = int(input("enter number : "))
# print(natural_num_sum(x))


x = int(input("Enter a natural number = "))
def sum_of_natural(x):
    ss = 0
    for i in range(1,x):
        ss = ss+(i*i)
    return ss
print("Sum of square of natural numbers are = " , sum_of_natural(x))
