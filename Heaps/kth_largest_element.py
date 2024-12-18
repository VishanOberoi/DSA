import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        #now we have a heap of k elements.

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
