class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        left, right = 0, n-1

        while left <= right:
            m = (left + right) // 2
            if target == nums[m]: return m
            elif nums[m] < target: left = m + 1
            else: right = m - 1
        
        return -1