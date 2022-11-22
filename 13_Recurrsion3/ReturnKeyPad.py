
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

def keypad(n):

    if n == 0:
        output = []
        output.append("")
        return output

    smallNum = n//10
    lastDig = n%10

    smalloutput = keypad(smallNum)

    optionForlastDigit = getString(lastDig)

    output1 = []

    for s in smalloutput:
        for c in optionForlastDigit:
            option = s + c
            output1.append(option)
    return output1

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)