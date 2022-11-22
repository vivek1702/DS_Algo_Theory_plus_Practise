import string


def PairStar(n):
    if len(n) == 0 or len(n) == 1:
        return n[0]
    
    if n[0] == n[1]:
        return n[0] + "*" + PairStar(n[1:])
    else:
        return n[0] + PairStar(n[1:])

n = string(input())
print(PairStar(n))