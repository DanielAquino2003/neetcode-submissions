class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        solution = [0] * l
        stack = []

        for i in range(l):
            if not stack or stack[-1][0] > temperatures[i]:
                stack.append((temperatures[i],i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    n = stack.pop()
                    solution[n[1]] = i-n[1]
                stack.append((temperatures[i],i))

        return solution