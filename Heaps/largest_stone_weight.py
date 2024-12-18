import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        #a minheap exits in python, but we need max.
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x!= y:
                heapq.heappush(stones, -abs(x-y))
        
        return -stones[0] if stones else 0