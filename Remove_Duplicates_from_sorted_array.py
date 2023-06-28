from __future__ import annotations
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,0,1,1,1,2,2,3,3,4]
        # stored = []
        # app = {}
        # for i in range(len(nums)):
        #     if nums[i] not in stored:
        #         stored.append(nums[i])
        #         app[nums[i]] = 0
        
        # j = 0
        # while j < len(nums):
        #     if 0 not in list(app.values()):
        #         break
        #     elif app[nums[j]] == 0:
        #         app[nums[j]] += 1
        #         j += 1
        #     else:
        #         if app[nums[j]] > 1:
        #             continue
        #         else:
        #             temp = nums.pop(j)
        #             nums.append(temp)

        # return j
        nums[:] = sorted(set(nums))
        return len(nums)
    

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(s.removeDuplicates([1,1,2]))