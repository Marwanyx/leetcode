from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = []

        while l <= r:
            x = -(nums[l] + nums[r])

            if x in nums and nums.index(x) != l and nums.index(x) != r:
                res.append([nums[l], nums[r], x])
                l += 1
            elif x > 0:
                l += 1
            elif x < 0:
                r -= 1
            else:
                l += 1
        
        return res


s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4])) # Expected: [[-1, -1, 2], [-1, 0, 1]]