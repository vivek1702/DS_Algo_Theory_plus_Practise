from itertools import permutations

def allpermutations(string):
    #Implement Your Code Here
    permList = permutations(string)
 
     # print all permutations
    for perm in list(permList):
        print (''.join(perm))


string = input()
allpermutations(string)