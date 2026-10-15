class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'{', '[', '('}
        closeBrackets = {'}', ')', ']'}
        for char in s:
            if char in brackets:
                stack.append(char)
            elif char in closeBrackets:
                bracket = self.getOpen(char)
                if not stack:
                    return False
                aux = stack.pop()
                if aux != bracket: return False
        return not stack

    
    def getOpen(self, s:str):
        if s ==')': return '('
        elif s == '}': return '{'
        elif s == ']': return '['
        return
    