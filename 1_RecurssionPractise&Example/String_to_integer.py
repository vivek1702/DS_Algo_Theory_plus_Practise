# def string_to_int(n):
#     num = int(n)
#     return type(num)

# n = input()
# print(string_to_int(n))


def string_to_int(n):
    if len(n) == 1:
        return ord(n[0]) - ord('0')

    y = string_to_int(n[1:])

    x = ord(n[0]) - ord('0')
    x = x * (10**(len(n)-1)) + y
    
    return x
# n = input()
print(string_to_int("5674"))