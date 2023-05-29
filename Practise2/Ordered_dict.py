
# n = int(input())
# ordinary_dict = {}
# for i in range(0,n):
#     *name, price = input().split()
#     name = ' '.join(name)
#     price = int()
#     if name in ordinary_dict:
#         ordinary_dict[name] += price
#     else:
#         ordinary_dict[name] = price
    
# print(ordinary_dict)

from collections import OrderedDict

N = int(input())
items_dict = OrderedDict()

for i in range(N):
    *name, price = input().split()
    name = ' '.join(name)
    price = int(price)
    if name not in items_dict:
        items_dict[name] = price
    else:
        items_dict[name] += price
        
# for i,k in items_dict.items():
#     print(i, k)
print(items_dict)

