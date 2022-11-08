
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

def appendLastNToFirst(head, n):
    if n == 0 or head is None :
        return head
    fast = head
    slow = head 
    initialHead = head
    for i in range(n) :
        fast = fast.next
    while fast.next is not None : 
        slow = slow.next 
        fast = fast.next
    temp = slow.next 
    slow.next = None 
    fast.next = initialHead 
    head = temp 
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
print(length(head))
appendLastNToFirst(head, n=3)
printLL(head)
