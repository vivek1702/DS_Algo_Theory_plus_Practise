import heapq
li = [1,5,4,7,6, 11]

heapq.heapify(li)
print(li)

heapq.heappush(li, 3)
print(li)

#heap max function
heapq._heapify_max(li)
print(li)

heapq.heapreplace(li, 0)