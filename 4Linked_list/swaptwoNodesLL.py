from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
	#Your code goes here
    x = i
    y = j
    if x == y:
        return

    # Search for x (keep track of prevX and CurrX)
    prevX = None
    currX = head
    count1 = 0
    while currX != None and count1 != x:
        prevX = currX
        currX = currX.next
        count1 += 1

    # Search for y (keep track of prevY and currY)
    prevY = None
    currY = head
    count2 = 0
    while currY != None and count2 != y:
        prevY = currY
        currY = currY.next
        count2 += 1

    # If either x or y is not present, nothing to do
    if currX == None or currY == None:
        return
    # If x is not head of linked list
    if prevX != None:
        prevX.next = currY
    else:  # make y the new head
        head = currY

    # If y is not head of linked list
    if prevY != None:
        prevY.next = currX
    else:  # make x the new head
        head = currX

    # Swap next pointers
    temp = currX.next
    currX.next = currY.next
    currY.next = temp

    return head




#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1