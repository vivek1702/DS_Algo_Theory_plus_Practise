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

def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def insert_recursively(head, i, data):
    if i < 0:
        return head

    if i == 0:
        newnode = node(data)
        newnode.next = head
        return newnode

    if head is None:
        return None

    small_head = insert_recursively(head.next, i-1, data)
    head.next = small_head
    return head

def lengthRecursive(head):
    if not head:
        return 0
    else:
        return 1+lengthRecursive(head.next)

def getcount(head):
    return lengthRecursive(head)

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
insert_recursively(head, i=2, data=11)
printLL(head)
print(getcount(head))