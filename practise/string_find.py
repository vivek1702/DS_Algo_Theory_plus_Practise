if __name__ == '__main__':
    s = input()
    lst = [False, False, False, False, False]
    for i in s:
        if i.isalnum():
            lst[0] = True
        if i.isalpha():
            lst[1] = True
        if i.isdigit():
            lst[2] = True
        if i.islower():
            lst[3] = True
        if i.isupper():
            lst[4] = True
                
    for each in lst:
        print(each)