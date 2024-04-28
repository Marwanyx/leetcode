from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result


s = Solution()
s.productExceptSelf([1, 2, 3, 4])