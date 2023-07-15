import numpy as np 

a = np.zeros((8,8), dtype=int)
a[1::2, 0::2] = 1
a[0::2, 1::2] = 1
print(a)
