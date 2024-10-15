import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        
        while left <= right:
            mid = (right + left) // 2
            time_to_eat = sum(math.ceil(pile/mid) for pile in piles) #time to eat all piles at rate = mid

            if time_to_eat > h:#then start eating more
                left = mid + 1
            if time_to_eat <= h:
                optimal = mid
                right = mid - 1
        return optimal            