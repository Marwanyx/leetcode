from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        i = 0
        if len(nums) == 1:
            return nums
        if not nums:
            return []
        while i + k <= len(nums):
            temp = nums[i:i + k]
            res.append(max(temp))
            i += 1

        return res
    
s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(s.maxSlidingWindow([1], 1))
print(s.maxSlidingWindow([1,-1], 1))