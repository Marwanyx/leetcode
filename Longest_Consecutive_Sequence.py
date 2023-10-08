from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()

        count = 0
        res = []
        for i in range(len(nums) - 1):
            if nums[i+1] - 1 != nums[i]:
                res.append(count + 1)
                count = 0
            else:
                count += 1
        res.append(count + 1)
        return max(res)

s = Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(s.longestConsecutive([100,4,200,1,3,2])) # 4
print(s.longestConsecutive([0,0])) # 1
print(s.longestConsecutive([1,2,0,1])) # 3
print(s.longestConsecutive([]))
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])) # 7