from os import *
from sys import *
from collections import *
from math import *

def getString(d):
    if d == 2:
        return "abc"

    if d == 3:
        return "def"

    if d == 4:
        return "ghi"

    if d == 5:
        return "jkl"

    if d == 6:
        return "mno"

    if d == 7:
        return "pqrs"

    if d == 8:
        return "tuv"

    if d == 9:
        return "wxyz"

def printKeypad(n,outputSoFar):
    if n == 0:
        print(outputSoFar)
        return 

    smallNum = n//10
    lastDig = n%10

    optionForlastDigit = getString(lastDig)

    for c in optionForlastDigit:
        newOtput = c + outputSoFar
        printKeypad(smallNum, newOtput)
    

n = int(input())
printKeypad(n,outputSoFar="")
