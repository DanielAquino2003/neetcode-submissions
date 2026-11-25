class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        left, right = 0, 0
        total = 0
        numbers = set()
        for right in range(0, len(s)):
            if s[right] not in numbers:
                numbers.add(s[right])
                total = max(total, right-left+1)
            else:
                while s[left] != s[right]: 
                    numbers.remove(s[left])
                    left+=1
                left+=1
        return total