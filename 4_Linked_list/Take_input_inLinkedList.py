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



def take_input():
    input_list = [int(ele) for ele in input().split()]
    head = None
    for currentData in input_list:
        if currentData == -1:
            break

        new_node = node(currentData)
        if head is None:
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    return head

head = take_input()
printLL(head)
print(length(head))