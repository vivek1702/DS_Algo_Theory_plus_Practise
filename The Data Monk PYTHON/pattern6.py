#abcdef
#abcde
#abcd
#abc
#ab
#a

for i in range(6, 0, -1):
    for i in range(65, 65+i):
        print(chr(i), end='')
    print()