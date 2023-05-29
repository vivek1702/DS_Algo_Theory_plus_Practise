from itertools import permutations

n = input().split()

m = [i for i in n[0]]
k = list(permutations(sorted(m), int(n[1])))
for i in k:
    b = ''.join(i)
    print(b.upper())
    


