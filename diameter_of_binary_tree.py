# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def depth(root):
            if root is None:
                return 0
            left = depth(root.left)
            right = depth(root.right)

            diameter_tree = left + right

            max_diameter[0] = max(max_diameter[0], diameter_tree)

            return 1 + max(left, right)

        depth(root)
        return max_diameter[0]
        
        