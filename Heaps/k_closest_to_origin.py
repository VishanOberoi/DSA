import math
import heapq
class Solution:
    def kClosest(self, points, k):
        kHeap = [] #an empty array, converts to heap when ops used.

        for x,y in points:
            dist = -(math.sqrt(x**2 + y**2))
            heapq.heappush(kHeap, [dist, x, y])

            if len(kHeap) > k:
                heapq.heappop(kHeap)
                
        
        return [[x,y] for _,x,y in kHeap]


        