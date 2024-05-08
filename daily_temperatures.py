from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = len(temperatures) * [0]
        i = 0
        j = 0
        while i < len(temperatures):
            if not stack:
                stack.append(temperatures[i])
                j = i
                i += 1
            else:
                item = stack.pop()
                if temperatures[i] > item:
                    stack.append(temperatures[i])
                    result.insert(j, i - j)
                    i += 1
                else:
                    stack.append(temperatures[i])
                    i += 1

        return result


s = Solution()

print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) # Expected: [1, 1, 4, 2, 1, 1, 0, 0]