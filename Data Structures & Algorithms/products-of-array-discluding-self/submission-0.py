class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        mult = 1
        for i in range(length):
            result[i] = mult
            mult = nums[i] * mult
        mult=1
        for i in range(length-1, -1, -1):
            result[i] = result[i] * mult
            mult = nums[i] * mult
        return result
