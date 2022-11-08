class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def countno(head):
    c=0
    global i
    while head!=None:
        if i==c:
            print(head.data)
            return
        c+=1
        head=head.next
    return 
        
def createll(li):
    head=None
    for ele in li:
        if ele==-1:
            break
        newnode=Node(ele)
        if head is None:
            head=newnode
            temp=head
        else:
            temp.next=newnode
            temp=temp.next
    return countno(head)

t=int(input())
for i in range(t):
    li=[int(x) for x in input().split()]
    i=int(input())
    createll(li)