
n = int(input())
s = set([int(x) for x in input().strip().split()]) 
for _ in range(int(input())):

    a = list(input().strip().split())

    if a[0] == 'pop':
        s.pop()
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    else:
        s.remove(int(a[1]))

print(sum(s))

#try to make dictinoary and implement it
# here we give set and remove the elements of set as per input given
#like
# input == pop the set.pop() or input == remove then set.remove()
#input format is like:


#5
#{1, 2, 3, 4, 5}
#operations = 4
#pop
#remove 4
#discard 3
#pop
