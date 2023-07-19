# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

def repeatedSubstringPattern(s: str):
    str1 = s[1:] + s[:-1]
    print(str1)
    if s in str1:
        return True
    return False
    
    
        


# a = 'abca'
a = "ababba"
# a = 'abab'
print(repeatedSubstringPattern(a))