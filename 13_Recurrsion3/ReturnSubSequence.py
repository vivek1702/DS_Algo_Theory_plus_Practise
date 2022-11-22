def subsequences(string):

    if len(string) == 0:
        output = []
        output.append("")
        return output

    smallstr = string[1:]
    smalloutput = subsequences(smallstr)
    output1 = []

    for sub in smalloutput:
        output1.append(sub)

    for sub in smalloutput:
        subs_with_zero_care = string[0] + sub
        output1.append(subs_with_zero_care)
    return output1



string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)