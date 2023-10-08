from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)

        while first < last:
            mid = (first + last) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                first = mid + 1

            else:
                 last = mid

        return first

s = Solution()
print(s.searchInsert([1,3,5,6], 7))
