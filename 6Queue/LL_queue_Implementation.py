from sys import stdin


#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self) :
        #Implement the getSize() function
        return self.count
        



    def isEmpty(self) :
        #Implement the isEmpty() function
        if self.count==0:
            return True
        else:
            return False



    def enqueue(self, data) :
        #Implement the enqueue(element) function
        newnode = Node(data)
        
        if self.head is None:            
            self.head = newnode
        else:
            self.tail.next = newnode
            
        self.tail = newnode   
        self.count = self.count + 1

        

    def dequeue(self) :
        #Implement the dequeue() function
        if self.head is None:
            return -1
        
        d = self.head.data
        self.head = self.head.next
        self.count = self.count - 1
        
        return d



    def front(self) :
        #Implement the front() function
        if self.head is None:
            return -1
        d = self.head.data
        return d
        
        
        




#main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1