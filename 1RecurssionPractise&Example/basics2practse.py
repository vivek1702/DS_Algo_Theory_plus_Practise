#rplace the charcater 
# def replacr_char(s, a, b):
#     if len(s) == 0:
#         return s

#     rv = replacr_char(s[1:], a, b)
#     if s[0] == a:
#         return b + rv
#     else:
#         return s[0] + rv

# print(replacr_char("abccddxx", 'c', 'x'))

###################################################################################

# remove x character from string
# def removeX(string): 
#     if len(string) == 0:
#         return string

#     rv = removeX(string[1:])
#     if string[0] == 'x':
#         return rv
#     else:
#         return string[0] + rv

# print(removeX("abcxdxe"))

#####################################################################################

# def replace_Pi(s):
#     if len(s) == 0:
#         return s

#     if s[0] == 'p' and s[1] == 'i':
#         rv = replace_Pi(s[2:])
#         return '3.14' + rv
#     else:
#         rv = replace_Pi(s[1:])
#         return s[0]+rv

# print(replace_Pi('abpibb'))

######################################################################################

# def removeConsecutiveDuplicates(string):
#     # Please add your code here
#     if len(string) < 2:
#         return string

#     if string[0] == string[1]:
#         rv = removeConsecutiveDuplicates(string[1:])
#         return rv
        
#     else:
#         rv = removeConsecutiveDuplicates(string[1:])
#         return string[0]+rv
    
# print(removeConsecutiveDuplicates("aabccdeef"))












