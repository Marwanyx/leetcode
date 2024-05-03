from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
s = Solution()
print(s.search([-1,0,3,5,9,12], 9)) # 4
print(s.search([-1,0,3,5,9,12], 2)) # -1
print(s.search([5], 5)) # 0
