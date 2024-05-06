from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack.pop()
                





s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"])) # Expected: 9

print(s.evalRPN(["4", "13", "5", "/", "+"])) # Expected: 6

print(s.evalRPN(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"])) # Expected: 22