# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.


def strStr(haystack: str, needle: str):
    indexx = -1
    for i in range(len(haystack)):
        str1 = haystack[i:i+len(needle)]
        if str1 == needle:
            indexx = i 
            break

    return indexx

#approach 2
    # if haystack == "" and needle == "":
    #         return 0
    #     else:
    #         if needle in haystack:
    #             return haystack.index(needle)
    #         else:
    #             return -1
        

haystack = 'hello'
needle = 'll'
# haystack = "leetcode"
# needle = "leeto"
# haystack = "sadbutsad" 
# needle = "sad"
print(strStr(haystack, needle))