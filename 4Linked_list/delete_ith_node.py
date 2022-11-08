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

def deleteNode(head, pos):

    curr = head
    prev = None
    count = 0
    while count < pos:       
        prev = curr
        curr = curr.next
        count += 1

    prev.next = curr.next
    return head

def deleteNodeRec(head, pos):
    if pos < 0:
        return head

    if head is None:
        return None


    if pos == 0:
        res = head.next
        return res


    small_head = deleteNodeRec(head.next, pos-1)
    head.next = small_head
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
deleteNodeRec(head, pos=1)
printLL(head)