class Solution:
    def search(self, nums, target):
        left, right = 0, len(target) - 1
        while left <= right:
            mid = (right + left) // 2
            #mid = right + (left - right)//2 prevents overflow error in other languages.
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1