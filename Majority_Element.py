from __future__ import annotations
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        app = {}

        for i in range(len(nums)):
            if nums[i] in app:
                app[nums[i]] += 1
            else:
                app[nums[i]] = 1

        for key, val in app.items():
            if val > len(nums)/2:
                return key
            

s = Solution()
print(s.majorityElement([3,2,3]))