def reverseString(s):
    
    def auxillary(s, lv, rv):
        if lv >= rv:
            return

        s[lv], s[rv] = s[rv], s[lv]

        auxillary(s, lv+1, rv-1)


    auxillary(s, 0, len(s)-1)

#################################################

    # if len(s) == 0:
    #     return s
    # else:
    #     return reverseString(s[1:]) + s[0]


print(reverseString("hello"))