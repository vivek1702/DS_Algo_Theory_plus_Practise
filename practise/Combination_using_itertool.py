from itertools import combinations, permutations

n = input().split()

m = [i for i in n[0]]
for i in range(1, int(n[1])+1):
    for j in list(combinations(sorted(m), i)):
        b = ''.join(j)
        print(b.upper())