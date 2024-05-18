class Solution:
    def isValid(self, s: str) -> bool:
        comp = {'{':'}','[':']','(':')'}
        left = {'{','[','('}
        stack = []
        for x in s:
            if x in left:
                stack.append(x)
            elif stack and comp[stack[-1]] == x:
                stack.pop()
            else:
                return False
        return not stack
