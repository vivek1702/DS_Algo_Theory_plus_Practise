# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Input: jewels = "z", stones = "ZZ"
# Output: 0


def numJewelsInStones(jewels, stones):
    count = 0
    d = {}
    for i in stones:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for i in jewels:
        if i in d.keys():
            count += d[i]

    return count



jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))