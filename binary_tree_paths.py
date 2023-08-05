from __future__ import annotations
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        r = self.helper(root)
        return r


    def helper(self, root) -> Optional[str]:
        res = ''
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return f'{root.val}'
        
        res += f'{root.val}->'
        temp = self.helper(root.left)
        if temp is not None:
            res += temp
        temp = self.helper(root.right) 
        if temp is not None:
            res += temp

        return res
    

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(s.binaryTreePaths(root))

