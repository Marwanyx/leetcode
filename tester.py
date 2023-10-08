from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
# Input: root = [1,2]
# Output: 1

# q: why is output 1
# a: because the longest path is 1
# q: how is it the longest path
# a: because the longest path is 1
# q: show an example
# a: [1,2]
# q: why is output 1
# a: because the longest path is 1
