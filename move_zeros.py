from __future__ import annotations
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            if nums[slow] != 0:
                slow += 1

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
        
        for j in range(count):
            nums.remove(0)
        
        for k in range(count):
            nums.append(0)
            


s = Solution()
num = [0,1,0,3,12]
s.moveZeroes(num)
print(num)
