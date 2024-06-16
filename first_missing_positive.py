from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(1)
        
        # replace all negative numbers with 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            if 1 <= nums[i] <= len(nums):
                val = abs(nums[i])
                
                if 
        

s = Solution()
print(s.firstMissingPositive([1,2,0])) # Expected output: 3