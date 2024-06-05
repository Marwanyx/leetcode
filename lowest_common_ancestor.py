from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val and root.val == q.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
    

s = Solution()

# root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = TreeNode(2)
q = TreeNode(4)

print(s.lowestCommonAncestor(root, p, q).val) # 2

