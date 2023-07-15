# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

x = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

#sort(), we can use this to sort the function by accessing 1 index of tuple

x.sort(key=lambda d: d[1])
print(x)
    