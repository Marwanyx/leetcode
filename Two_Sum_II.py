from __future__ import annotations
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]

            if total == target:
                return [i+1, j+1]
            elif total > target:
                j -= 1
            elif total < target:
                i += 1


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]