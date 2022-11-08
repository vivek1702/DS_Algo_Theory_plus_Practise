from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    #Your code goes here
    evenStart = None
     
    # Ending node of even values list.
    evenEnd = None
     
    # Starting node of odd values list.
    oddStart = None
     
    # Ending node of odd values list.
    oddEnd = None
     
    # Node to traverse the list.
    currNode = head
     
    while(currNode != None):
        val = currNode.data
         
        # If current value is even, add
        # it to even values list.
        if(val % 2 == 0):
            if(evenStart == None):
                evenStart = currNode
                evenEnd = evenStart
            else:
                evenEnd.next = currNode
                evenEnd = evenEnd.next
         
        # If current value is odd, add
        # it to odd values list.
        else:
            if(oddStart == None):
                oddStart = currNode
                oddEnd = oddStart
            else:
                oddEnd.next = currNode
                oddEnd = oddEnd.next
                 
        # Move head pointer one step in
        # forward direction
        currNode = currNode.next
     
    # If either odd list or even list is empty,
    # no change is required as all elements
    # are either even or odd.
    if oddStart == None:
        return evenStart 
    if evenStart == None:
        return oddStart
     
    # Add odd list after even list.    
    oddEnd . next = evenStart
    evenEnd . next = None
     
    # Modify head pointer to
    # starting of even list.
    head = oddStart

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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1