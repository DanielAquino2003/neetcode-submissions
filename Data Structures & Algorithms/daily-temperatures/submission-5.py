class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        solution = [0] * l
        stack = []

        for i in range(l):
            if not stack or temperatures[stack[-1]]> temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    n = stack.pop()
                    solution[n] = i-n
                stack.append(i)

        return solution