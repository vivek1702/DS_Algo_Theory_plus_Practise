# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

def string_shuffle(s, indices):
    res = [''] * len(s)
    for i, char in enumerate(s):
        res[indices[i]] = char

    return res



# s = "abc"
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(string_shuffle(s, indices))