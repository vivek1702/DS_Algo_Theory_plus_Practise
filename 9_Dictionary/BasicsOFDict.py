a = {1:2, 3:4, "list":2}
# print(a)
# print(a['list'])
# print(a.get(1))
# print(a.get("li")) #some times get() fails because we didn't mention and "li" dictinary before and it geives none value of it
# print(a.keys())
# print(a.values())
# print(a.items())

#by default it print keys value
for i in a:
    print(i)

#this will give keys and values
for i in a:
    print(i, a[i])

#this will gives us values
for i in a.values():
    print(i)

#this will give weather keys in dictinary or not 
print('list' in a)

# print(a[0])

# We can make use of this feature in another way. 
# Say we want the method to do the following action: 
# If the key is present in the dictionary then return the value corresponding to the key. 
# In case the key is not present, return a custom desired value ( say 0 ).
d = {1:2, 'abc':5, 'def':7}
print(d.get(0,3))

a ['tup'] = ('1, 2, 3')
print(a)

#to clear dictionary
a.clear()

#to delete dictionary
del a