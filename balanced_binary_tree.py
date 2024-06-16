from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            left = self.depth(root.left)
            right = self.depth(root.right)

            if abs(right - left) > 1:
                return False
            
            return self.isBalanced(root.left) and self.isBalanced(root.right) 

    def depth(self, node) -> int:
        if node is None:
            return 0
        else:
            return 1 + max(self.depth(node.left), self.depth(node.right))
        
s = Solution()
print(s.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == True) # Expected output: True