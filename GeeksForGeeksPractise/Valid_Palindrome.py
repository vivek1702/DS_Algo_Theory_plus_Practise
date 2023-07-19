#here we check the phrase for valid palindrome 


import re

def isPalindrome(s):
    new_str = re.sub(r'[^\w]|_','',s).lower()
    reverse_word = new_str[::-1]

    return reverse_word == new_str
    # if new_str == reverse_word:
    #     return True
    # else:
    #     return False
    

# s = "ab_a"
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.