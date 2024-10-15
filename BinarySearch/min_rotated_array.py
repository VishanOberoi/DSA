class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        res= float('inf') #can be any element

        while left <= right:

            if nums[right] > nums[left]:
                #we are in an ascending part
                res = min(res, nums[left])
            
            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[left]:
                #mid is a part of the left side
                left = mid + 1
            else:
                right = mid -1
        return res
            
