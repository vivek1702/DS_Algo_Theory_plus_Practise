ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = map(list, filter(lambda x: x%2 == 0, ll))   #code as oddlist for proper output
odd_list = list(filter(lambda x: x%2 != 0, ll))

print(even_list)
print(odd_list)