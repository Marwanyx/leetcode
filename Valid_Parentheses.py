class Solution:
    def isValid(self, s: str, l: int) -> bool:
        stack = []
        count = 0
        for char in s:
            if char not in "({[)}]":
                continue

            count += 1
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                
                item = stack.pop()
                if char == ")" and item == "(":
                    continue
                elif char == "}" and item == "{":
                    continue
                elif char == "]" and item == "[":
                    continue
                else:
                    return False
        
        return len(stack) == 0 and count == l


s = Solution()
print(s.isValid("()", 2)) # True
print(s.isValid("()[]{}", 2)) # False
print(s.isValid("(]", 2)) # False