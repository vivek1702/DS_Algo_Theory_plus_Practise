# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.


def finalValueAfterOperations(str):
    X = 0
    for i in str:
        if i == '--X' or i == 'X--':
            X -= 1
        else:
            X += 1
    
    return X


input = ["++X","++X","X++"]
# ["--X","X++","X++"]
print(finalValueAfterOperations(input))