from __future__ import annotations
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        dct = {}
        self.helper(root, dct)
        m = max(dct.values())
        r = []
        for key, val in dct.items():
            if val == m:
                r.append(key)
        return r
            
    def helper(self, root, dct) -> None:
        if root is None:
            return
        if root.val in dct:
            dct[root.val] += 1
        else:
            dct[root.val] = 0

        self.helper(root.left, dct)
        self.helper(root.right, dct)
        return
    

s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
print(s.findMode(root))