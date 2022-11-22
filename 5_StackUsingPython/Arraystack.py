class stack:
    
    def __init__(self):
        self.__data  = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            return
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return
        return self.__data[len(self.__data)-1]
            
    def size(self):
        len(self.__data)

    def isEmpty(self):
        return self.size() == 0


s = stack()
s.push(13)
s.push(14)
s.push(14)

print(s.pop())
print(s.pop())