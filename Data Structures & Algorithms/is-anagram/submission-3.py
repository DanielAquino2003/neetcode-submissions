class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        d1={}
        for char in s:
            d1[char] = d1.get(char, 0) + 1

        for char in t:
            if char not in d1 or d1[char] == 0: return False
            else: d1[char] -= 1
        
        return True