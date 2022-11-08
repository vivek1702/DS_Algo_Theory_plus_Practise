import abc


class MapNode:
    def __init__(self, key, value) -> None:
        self.value = value
        self.key = key
        self.next = None

class Map:
    def __init__(self) -> None:
        self.bucketsize = 10
        self.bucket = [None for i in range(self.bucketsize)]
        # for i in range(self.bucketsize):
        #     self.bucket = [None]
        self.count = 0

    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return (abc(hc)%(self.bucketsize))

    def rehash(self):
        temp = self.bucket
        self.bucket = 2 *[None for i in range(self.bucketsize)]
        self.bucketsize = 2 * self.bucketsize
        self.count = 0
        for head in temp:
            while head is not None:
                self.Insert(head.key, head.value)
                head = head.next
                

    def Insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next


        head = self.bucket[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.bucket[index] = newNode
        self.count += 1
        
        load_Factor = self.count/self.bucketsize
        if load_Factor >= 0.7:
            self.rehash()

    def getvalue(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]

        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        return None

    def remove(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.bucket[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1
                return head.value

            prev = head
            head = head.next

        return None


m = Map()
m.Insert("vivek", 2)
print(m.size())

