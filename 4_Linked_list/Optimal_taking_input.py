
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

def printIthNode(head, i):
    count = 0
    while head is not None:
        if count == i:
            return str(head.data)
        count += 1
        head = head.next


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
print(printIthNode(head, i=10))