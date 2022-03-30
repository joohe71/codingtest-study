import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    answer = 0
    while (heap[0] < K):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b*2)
        answer +=1
        if len(heap) == 1 and heap[0] < K:
            return -1
    return answer