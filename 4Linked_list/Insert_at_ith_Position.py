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

def insert_at_i_position(head, i, data):
    if i < 0 or i > length(head):
        return head

    curr = head
    prev = None
    count = 0
    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    newnode = node(data)
    if prev is not None:
        prev.next = newnode
    else:
        head = newnode
    newnode.next = curr
        
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
insert_at_i_position(head, i=2, data=11)
printLL(head)