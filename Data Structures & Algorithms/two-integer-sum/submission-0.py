class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        solution = []
  
        for i in range(len(nums)):
            aux = target - nums[i]
            if aux in pairs:
                solution.append(pairs[aux])
                solution.append(i)
            else:
                pairs[nums[i]] = i
        return solution