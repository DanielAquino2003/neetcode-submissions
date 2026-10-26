class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                total = b+a
                stack.append(total)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                total = b-a
                stack.append(total)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                total = b*a
                stack.append(total)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                if a==0:
                    total = 0
                else:
                    total = int(b/a)
                stack.append(total)  
            else:
                token = int(token)
                stack.append(token)
        
        result = stack.pop()
        return result