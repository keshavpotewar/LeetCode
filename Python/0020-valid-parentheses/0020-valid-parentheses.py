class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        valid = ['(','[','{']

        for ch in s :
            if ch in valid:
                stack.append(ch)
            else:
                  if len(stack) == 0:
                    return False
                  if ch == ')' and stack[-1] != '(':
                    return False
                  if ch == ']' and stack[-1] != '[':
                    return False    
                  if ch == '}' and stack[-1] != '{':
                    return False
                  
                  stack.pop()
        
        return len(stack) == 0