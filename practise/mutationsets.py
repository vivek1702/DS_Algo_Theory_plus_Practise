n = int(input())
s = set(map(int, input().split()))
print(s)
operations_perform = int(input())
for i in range(0,operations_perform):
    m = input().split()
    if m[0] == 'intersection_update':
        s1 = int(m[1])
        s1 = set(map(int, input().split()))
        s.intersection_update(s1)

    elif m[0] == 'update':
        s2 = int(m[1])
        s2 = set(map(int, input().split()))
        s.update(s2)

    elif m[0] == 'symmetric_difference_update':
        s2 = int(m[1])
        s2 = set(map(int, input().split()))
        s.symmetric_difference_update(s2)

    elif m[0] == 'difference_update':
        s2 = int(m[1])
        s2 = set(map(int, input().split()))
        s.difference_update(s2)

set_sumss = list(s)  
print(sum(set_sumss))
