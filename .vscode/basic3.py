from cmath import inf


def Geometric_Sum(k):
    if k == 0:
        return 1
    
    return 1/pow(2, k) + Geometric_Sum(k -1)

print(Geometric_Sum(3))