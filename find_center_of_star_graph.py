from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        common = -1
        for i in range(len(edges)):
            edges[i] = set(edges[i])

        for j in range(len(edges) - 1):
            common = edges[j] & edges[j + 1]

        return common.pop()
    
s = Solution()
print(s.findCenter([[1,2],[2,3],[4,2]]))
