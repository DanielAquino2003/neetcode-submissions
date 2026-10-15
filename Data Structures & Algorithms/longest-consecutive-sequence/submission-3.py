class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Non efficient: for each position y search if thre is a n-1, n-2, etc... until false y voy actualizando la longitud
        numbers = set(nums)
        maximum = 0
        last = 0
        first = 0
        for num in nums:
            i = 0
            total=0
            if num <= first or num >= last:
                while num+i in numbers:
                    total+=1
                    i+=1
                print(f"total for num {num} is : {total}")
                if total > maximum:
                    last = num+i-1
                    first = num
                    maximum = total

        return maximum
            