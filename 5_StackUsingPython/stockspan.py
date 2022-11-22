from sys import stdin

def stockSpan(price, n) :
	#Your code goes here
    s = [None]*n
    s[0] = 1
    for i in range(1, n):
        s[i] = 1

        j = i -1
        while j>=0 and price[i] >= price[j]:
            s[i] += 1
            j -= 1

    return s

#   n = len(price)
    # Create a stack and push index of first element to it
    st = [] 
    st.append(0)
  
    # Span value of first element is always 1
    S[0] = 1
  
    # Calculate span values for rest of the elements
    for i in range(1, n):
          
        # Pop elements from stack while stack is not
        # empty and top of stack is smaller than price[i]
        while( len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()
  
        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i] is
        # greater than elements after top of stack
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1])
  
        # Push this element to stack
        st.append(i) /*


def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)