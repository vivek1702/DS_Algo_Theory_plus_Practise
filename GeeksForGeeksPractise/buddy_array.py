def buddyStrings(s, goal):

    if s == goal:
        return True # for swapping same character 
    
    i = 0
    j = len(s)-1 
    while i < j and s[i] == goal[i]:
        i += 1 

    while j >= 0 and s[j] == goal[j]:
        j -= 1 


    if i < j:
        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        s = ''.join(s_list)

    return s

    

# Inputs: 
# s = "abcd" 
# goal = "cbad"
 #True

s = 'aa'  
goal = 'aa'
print(buddyStrings(s, goal))
#output = True

# s = 'ab'
# goal = 'ab
#output False

# /* First, it checks if s is equal to goal using the == operator. If they are equal, it means the strings are identical.

# If s is equal to goal, the code creates a temporary set called temp to store the unique characters present in s.
#  It does this by converting the string s to a set of characters using the set constructor.

# The code then returns the result of the comparison temp.size() < goal.size(). 
# This comparison checks if the size of the set temp (number of unique characters in s) is less than the size of the string goal.
#  If it is, it means there are duplicate characters in s, and swapping any two of them would result in s becoming equal to goal. In this case, 
# the function returns true; otherwise, it returns false.

# If s is not equal to goal, the code proceeds to find the indices i and j such that s[i] and goal[i] are the first pair of characters that are different from each other 
# when scanning from the left, and s[j] and goal[j] are the first pair of characters that are different from each other when scanning from the right.

# The code uses a while loop to increment the i index from left to right until it finds a mismatch between s[i] and goal[i]. 
# Similarly, it uses another while loop to decrement the j index from right to left until it finds a mismatch between s[j] and goal[j].

# After finding the mismatched indices, the code checks if i is less than j. If it is, 
# it means there is a pair of characters that can be swapped to make s equal to goal. In this case, the code uses the swap function to swap the characters s[i] and s[j].

# Finally, the code checks if s is equal to goal after the potential swap. If they are equal,
#  it means we have successfully swapped two characters to make s equal to goal, and the function returns true. Otherwise, it returns false.

# /*