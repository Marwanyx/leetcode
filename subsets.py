from  typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        elif isinstance(nums, int):
            return [nums]
        else:
            lst = []
            for num in nums:
                if isinstance(nums, list):
                    lst.extend(self.subsets(num))
                else:
                    lst.append(self.subsets(num))

            return lst
        

s = Solution()

print(s.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]