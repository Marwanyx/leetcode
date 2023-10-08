from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        t = 1
        t2 = 1
        for i in range(len(nums)):
            t *= nums[i]

        if nums.count(0) == 1:
            for k in range(len(nums)):
                if nums[k] == 0:
                    t2 *= 1
                else:
                    t2 *= nums[k]
        elif nums.count(0) > 1:
            return [0]*len(nums)

        for j in range(len(nums)):
            if nums[j] == 0:
                res.append(t2)
            else:
                res.append(t//nums[j])

        return res
    
s = Solution()
print(s.productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(s.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
print(s.productExceptSelf([0,0])) # [0,0]
