from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val} -> {self.left} -> {self.right}"
    
    def __str__(self) -> str:
        return f"{self.val} -> {self.left} -> {self.right}"

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        lst = []
        self.preorder_traversal(root, lst)
        root.left = None
        root.right = None

        root.val = lst[0]
        curr = root

        for val in lst[1:]:
            curr.right = TreeNode(val, None)
            curr = curr.right


    def preorder_traversal(self, root, lst):
        if root is None:
            return
        
        lst.append(root.val)
        self.preorder_traversal(root.left, lst)
        self.preorder_traversal(root.right, lst)


s = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
s.flatten(root)
print(root)

# class Solution2:
#     def __init__(self) -> None:
#         self.prev = None

#     def flatten(self, root: Optional[TreeNode]) -> None:
#         if root is None:
#             return
        
#         self.flatten(root.right)
#         self.flatten(root.left)
#         root.right = self.prev
#         root.left = None
#         self.prev = root


# s = Solution2()
# root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
# s.flatten(root)
# print(root)