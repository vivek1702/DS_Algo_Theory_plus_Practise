from sys import stdin


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def mergeTwoSortedLinkedLists(head1, head2):

    # Write your code here
    finalhead = Node(-1)
    finaltail = finalhead
    while True:
    
        if head1 is None:
            finaltail.next = head2
            break
            
        if head2 is None:
            finaltail.next = head1
            break
    
    
        if head1.data <= head2.data:
            finaltail.next = head1
            head1 = head1.next
        else:
            finaltail.next = head2
            head2 = head2.next
            
        finaltail = finaltail.next            
        
    return finalhead.next
            
    

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


# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1

printLinkedList(t)
