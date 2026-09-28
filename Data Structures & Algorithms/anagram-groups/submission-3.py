class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solutions = {}
        for s in strs:
            count = [0] * 26
            
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            key = tuple(count)
            
            if key in solutions:
                solutions[key].append(s)
            else:
                solutions[key] = [s]

        return list(solutions.values())