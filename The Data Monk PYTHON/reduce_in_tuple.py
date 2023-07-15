# from functools import reduce
# def add_str(a,b):
#     return a+' '+b

# a = ['the','Data','Monk', 'is', 'a', 'website', 'a']
# print(reduce(add_str, a))


# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))


# output
# The sum of the list elements is : 17
# The maximum element of the list is : 6