# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.


# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

def balancedStringSplit(s):
    count = 0
    st = []

    for char in s:
        if st == []:
            st.append(char)
            count += 1
        elif char == st[-1]:
            st.append(char)
        else:
            st.pop()


    return count


s = "RLRRLLRLRL"
"LLLLRRRR"

print(balancedStringSplit(s))


# we can solve this by stack greedy method