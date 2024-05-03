import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
            
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / mid)
            
            if total <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res