if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    seta = set(map(int, input().split()))
    setb = set(map(int, input().split()))

    count = 0

    for i in arr:
        if i in seta:
            count += 1
        elif i in setb:
            count -= 1

    print(count)
