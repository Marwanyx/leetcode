from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = 0
        res = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res.append(count)
                    break
                count += 1
            if count == len(temperatures) - i:
                res.append(0)
        return res

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))