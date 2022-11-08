import heapq
def kLargest(lst, k):
    pq = []
    heapq.heapify(pq)
    N = len(lst)
    for i in range(N):
 
        # Insert elements into
        # the priority queue
        heapq.heappush(pq, lst[i])
 
        # If size of the priority
        # queue exceeds k
        if (len(pq) > k):
            heapq.heappop(pq)
 
    return pq

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
