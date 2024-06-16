from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        largest = 0
        while l <= r:
            total = sum(nums[l: r + 1])

            largest = max(largest, total)

            if nums[l] < nums[r]:
                l += 1
            elif nums[l] >= nums[r]:
                r -= 1

        return largest


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # Expected output: 6

print(s.maxSubArray([1])) # Expected output: 1