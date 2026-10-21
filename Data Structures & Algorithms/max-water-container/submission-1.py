class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #distance = j - i 
        #total = distance * max(heights[i], heights[j])
        i, j = 0, len(heights)-1
        total = float("-inf")
        while i < j:
            distance = j - i
            aux = distance * min(heights[i], heights[j])
            if aux > total:
                total = aux
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return total