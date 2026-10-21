class Solution:
    def trap(self, height: List[int]) -> int:
        #i = 0, j=i+1
        # calculate height[i]-height[j] if positive, aggregate to aux, when height[i]-height[j] == 0 or negatie, we aggregate aux to the solution, and i = j and j+=1 and restart
        i = 0
        j = i+1
        total = 0
        length = len(height)

        while j<length:
            maximum = -1
            while j < length and height[j] < height[i]:
                if maximum == -1 or height[j] > height[maximum]:
                    maximum = j
                j+=1
            if j >= length:
                j = maximum
            if height[i]<height[j]: limit = height[i]
            else: limit = height[j]
            i+=1
            aux = 0
            while i < j:
                aux += limit - height[i]
                i+=1
            total+=aux
            j+=1
        return total 
