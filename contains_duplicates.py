from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
    

s = Solution()
print(s.containsDuplicate([1,2,3,1]))