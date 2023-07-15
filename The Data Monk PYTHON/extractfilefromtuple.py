from itertools import chain

list_1= [(97,98),(4,93),(0,1)]
x = map(lambda a: str(a), chain.from_iterable(list_1))

print(tuple(x))