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

def removeDuplicates(head):
    temp = head
    if temp is None:
        return
    while temp.next is not None:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = new
        else:
            temp = temp.next
    return head



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
removeDuplicates(head)
printLL(head)