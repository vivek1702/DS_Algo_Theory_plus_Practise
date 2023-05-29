def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    h = [alphabets[size-1]]
    s = h[0].center((size-1)*4+1,'-') + "\n"
    for x in range(size-1,0,-1):
        l = [*h]
        h.append(alphabets[x-1])
        k = [*h]
        k.extend(l[::-1])
        s += ('-'.join(k)).center((size-1)*4+1,'-') + "\n"
    
    f = s.split('\n')
    #Bot
    f = f[:-2:]
    for x in range(len(f)):
        s += f.pop() + "\n"
    print(s)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)