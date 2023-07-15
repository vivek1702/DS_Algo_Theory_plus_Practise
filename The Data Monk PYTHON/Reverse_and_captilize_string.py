#important hacker rank question unable to do it

def reverse_and_captilize(sentences):
    words = sentences.split()
    l = []
    for i in words:
        k = ''
        for j in i:
            if j.isupper() == True:
                j = j.lower()
            else:
                j = j.upper()
            k += j
        l.append(k)

    m = " ".join(reversed(l))
    return m

a = "aWESOME is cODING"
print(reverse_and_captilize(a))