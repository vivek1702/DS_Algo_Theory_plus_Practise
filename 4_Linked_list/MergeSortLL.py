from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def MergeTwoSorted(a, b):
    result = None

    if a == None:
        return b
    if b == None:
        return a

    if a.data <= b.data:
        result = a
        result.next = MergeTwoSorted(a.next, b)
    else:
        result = b
        result.next = MergeTwoSorted(a, b.next)

    return result

def mergeSort(head):
    if head == None or head.next == None:
        return head

    mid = middleval(head)
    nextToMid = mid.next
    mid.next = None

    left = mergeSort(head)
    right = mergeSort(nextToMid)

    sortedlist = MergeTwoSorted(left, right)
    return sortedlist


def middleval(head):
    if head == None:
        return head

    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow




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
        print(head.data, end = "->")
        head = head.next

    print()

head = takeInput()
printLinkedList(head)
print(mergeSort(head))
printLinkedList(head)

