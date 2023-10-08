from __future__ import annotations
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expected = nums[:]
        e = expected.count(val)
        i = 0
        while i + e != len(nums):
            if nums[i] == val:
                nums.append(nums[i])
                nums.pop(i)
            else:
                i += 1
        
        return i
            

s = Solution()
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))