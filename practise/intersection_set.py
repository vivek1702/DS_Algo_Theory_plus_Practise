n = int(input())
seta = set(map(int, input().split()))

m = int(input())
setb = set(map(int, input().split()))

print(seta)
print(setb)

a = seta.intersection(setb)
print(len(a))