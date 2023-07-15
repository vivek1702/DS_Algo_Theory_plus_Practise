def ispar(x):
    # code here
    stack = []
    for i in x:
        if (i == '(') or (i == '{') or (i == '['):
            stack.append(i)
        if (i == ')') or (i == '}') or (i == ']'):
            if stack:
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        return 'true'
    else:
        return 'false'
    
a = ispar(x=['(', '{', '[', ']'])
print(a)