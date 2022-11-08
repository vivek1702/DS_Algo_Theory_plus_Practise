class queue_using_two_stack:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        self.s1.append(data)

    def dequeue(self):

        while len(self.s1) != 1:
            self.s2.append(self.s1.pop())

        d = self.s1.pop()

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

        return d
    
q = queue_using_two_stack()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())


