from itertools import combinations_with_replacement

n = input().split()

m = [i for i in n[0]]
k = list(combinations_with_replacement(sorted(m), int(n[1])))
for i in k:
    b = ''.join(i)
    print(b.upper())