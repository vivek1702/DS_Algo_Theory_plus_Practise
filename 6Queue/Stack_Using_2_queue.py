from queue import Queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0

    def getSize(self):
        return self.curr_size
        # Implement the getSize() function

    def isEmpty(self):
        return self.curr_size == 0
        # Implement the isEmpty() function

    def push(self, data):
        self.curr_size += 1
        self.q1.put(data)
        # Implement the push(element) function

    def pop(self):
        if self.isEmpty():
            return -1
        self.curr_size -= 1
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        ele = self.q1.get()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return ele
        # Implement the pop() function

    def top(self):
        if self.isEmpty():
            return -1
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        ele = self.q1.get()
        self.q2.put(ele)
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return ele

    # Implement the top() function


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1