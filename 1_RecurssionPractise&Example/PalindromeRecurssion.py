def Palindrome_Num(s):
    n = len(s)

    if n == 0:
        return True

    return palindrome_check(s, 0, n-1)


def palindrome_check(s, a, b):
    if a == b:
        return True

    if s[a] != s[b]:
        return False

    if a < b+1:
        return palindrome_check(s, a+1, b-1)

    return True

# s = input("enter string ")
print(Palindrome_Num("abcba"))

#to solve palindrome we need to check base case first which is either length is 0 or 1 
#in this case its true

#second we create a another check function for palindrome where we do solution check
# like if first value is euqal to last value the we do increment in first value through index in another function 
# and decrement in from last index recurssive fucntion and again check
