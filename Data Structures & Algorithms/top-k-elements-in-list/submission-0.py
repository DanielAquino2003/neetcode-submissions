class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        solution = []


        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        

        for key, value in freqs.items():
            bucket[value].append(key)
            
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                solution.extend(bucket[i])
                
        
        return solution[:k] 
