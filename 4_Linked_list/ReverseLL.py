class node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end=' ')
        head = head.next
    print("None")
    return

def printReverse(head) :
    #Your code goes here
    if not head: 
        return head #Empty.
    if not head.next: 
        return head #We reached end.
    orig_head = printReverse(head.next) #Traverse to end, orig_head is now end node.
    head.next.next = head #Swap head with right node.
    head.next = None #So we don't wind up in infinite loop.
    return orig_head #Very last thing returned. End node!
    
    

def take_input():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currentData in inputList:
        if currentData == -1:
            break

        newNode = node(currentData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

head = take_input()
printLL(head)
printReverse(head)
printLL(head)
