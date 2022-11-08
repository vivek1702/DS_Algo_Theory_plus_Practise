class QueueArray:
    def __init__(self) -> None:
        self.__arr = []
        self.__count = 0
        self.__front = 0

    def enqueue(self, data):
        self.__arr.append(data)
        self.__count += 1

    def dequeue(self):
        if self.__count == 0:
            return -1
        ele = self.__arr[self.__front]
        self.__front += 1
        self.__count -= 1
        return ele

    def front(self):
        if self.__count == 0:
            return -1
        return self.__arr[self.__front]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

a = QueueArray()
a.enqueue(1)
a.enqueue(111)
a.enqueue(13)
a.enqueue(14)
while (a.isEmpty() is False):
    print(a.front())
    a.dequeue()

print(a.dequeue())

        


        
