from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        elif root.left and root.right:
            if root.left.val < root.val < root.right.val:
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            return False
        elif root.left and not root.right:
            if root.left.val < root.val:
                return self.isValidBST(root.left)
            return False
        elif not root.left and root.right:
            if root.val < root.right.val:
                return self.isValidBST(root.right)
            return False
        else:
            return False

s = Solution()

# Test case 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(s.isValidBST(root))  # Expected: True

# Test case 2
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

print(s.isValidBST(root))  # Expected: False