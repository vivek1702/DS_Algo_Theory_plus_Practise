# 4. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

d = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

d.sort(key= lambda x: int(x['model']))
print(d)