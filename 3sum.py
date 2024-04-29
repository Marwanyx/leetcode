from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

    
s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(s.threeSum([]))  # []
print(s.threeSum([0]))  # []