class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maximum = 0
        for num in nums:
            if num-1 not in numbers:
                i = 0
                total = 0
                while num+i in numbers:
                    total+=1
                    i+=1
                maximum = max(maximum, total)                

        return maximum
            