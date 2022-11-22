def printSubs(s, o):
    if len(s) == 0:
        print(o)
        return

    printSubs(s[1:], o)
    newoutput = o + s[0]
    printSubs(s[1:], newoutput)


s = input()
ans= printSubs(s, o="")