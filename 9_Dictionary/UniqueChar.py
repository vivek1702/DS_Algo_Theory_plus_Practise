def uniqueChar(s): 
    # Write your code here
    s=[char for char in s]
    st=''
    for i in s:
        if i in st:
            continue
        else:
            st+=i
    return st
    
        

# Main 
s=input() 
print(uniqueChar(s))