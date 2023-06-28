class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                if s[i] == ")":
                    return False
                elif s[i] == "}":
                    return False
                elif s[i] == "]":
                    return False
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == "{":
                stack.append(s[i])
            elif s[i] == "[":
                stack.append(s[i])

            elif s[i] == ")":
                if "(" == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif s[i] == "}":
                if "{" == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif s[i] == "]":
                if "[" == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("({{{{}}}))"))
print(s.isValid("(])"))