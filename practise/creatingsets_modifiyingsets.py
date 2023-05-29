if __name__ == '__main__':
    m = int(input())
    setm = set((map(int, input().split())))
    n = int(input())
    setn = set((map(int, input().split())))

    out = setm.symmetric_difference(setn)
    print(*out, sep ="\n")

    