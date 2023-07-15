def longestCommonPrefix(strs):
    longest_prefix = " "
    if len(strs) > 0:
        s = sorted(strs)
        first = s[0]
        last = s[-1]

        for i in range(len(first)):
            if len(last) > i and last[i] == first[i]:
                longest_prefix += first[i]
            else:
                return longest_prefix
            
    return longest_prefix


strs = ["dog","racecar","car"]
# strs =  ["flower","flow","flight"]
# Output: "fl"
print(longestCommonPrefix(strs))