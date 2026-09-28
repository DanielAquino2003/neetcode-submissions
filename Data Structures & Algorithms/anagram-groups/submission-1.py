class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solutions = {}
        for s in strs:
            count = [0] * 26
            
            for char in s:
                idx = ord(char) - ord('a')
                count[idx] += 1
                
            key = tuple(count)
            
            if key in solutions:
                solutions[key].append(s)
            else:
                solutions[key] = [s]

        return list(solutions.values())