

# def merge(a, b):
#     return (a.update(b))

# a = {'x':12,'y':34}
# b = {'z':34,'a':76}

# print(merge(a,b))
# print(b)


#another menthod

def merge(a, b):
    res = {**a, **b}
    return res

a = {'x':12,'y':34}
b = {'z':34,'a':76}

print(merge(a,b))

