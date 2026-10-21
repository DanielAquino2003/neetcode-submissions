class Solution:
    def trap(self, height: List[int]) -> int:
        #i = 0, j=i+1
        # calculate height[i]-height[j] if positive, aggregate to aux, when height[i]-height[j] == 0 or negatie, we aggregate aux to the solution, and i = j and j+=1 and restart
        length = len(height)
        left_max = [0] * length
        right_max = [0] * length

        left_max[0] = height[0]

        total = 0

        for i in range(1,length):
            left_max[i] = max(height[i], left_max[i-1])
        
        right_max[length - 1] = height[length - 1]
        for i in range(length-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        for i in range(length):
            aux = min(left_max[i], right_max[i]) - height[i]
            if aux > 0:
                total+=aux
        return total
