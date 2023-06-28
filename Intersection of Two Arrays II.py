from __future__ import annotations
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        apps = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                apps.append(nums1[i])
                nums2.remove(nums1[i])
        

        return apps
    
s = Solution()

s.intersect([1,2,2,1], [2,2])