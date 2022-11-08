# def reverseQueue(inputQueue) :
#     # Your code goes here
#     n = len(inputQueue)
#     arr = [0] * n

#     while inputQueue:
#         d  = inputQueue.pop()
#         arr.append(d)

#     for i in arr:
#         inputQueue.append(i)

#     return inputQueue


# print(reverseQueue([1, 2, 3]))

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    if inputQueue.qsize() <= 1 :
        return

    front = inputQueue.get()

    reverseQueue(inputQueue)

    inputQueue.put(front)



'''-------------- Utility Functions --------------'''



def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1