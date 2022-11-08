def printPairDiffK(l, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    d = {}

    paircount = 0

    for num in l:
        if num+k in d:
            paircount += d[num+k]
        if num-k in d and k!=0:
            paircount += d[num-k]
        
        # update map
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    return paircount
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))