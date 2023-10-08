from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # sort the hashmap by value, greater to smaller
        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_hashmap.keys())[:k]
    
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
        