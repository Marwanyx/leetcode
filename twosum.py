from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in dct:
                return [dct[diff], i]

            dct[nums[i]] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
