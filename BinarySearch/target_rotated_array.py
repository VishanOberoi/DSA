class Solution:
    def search(self, nums, target) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:  #mid is in the left sorted portion
                if target>nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else: #mid is in the right sorted porition
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
                
           

                
