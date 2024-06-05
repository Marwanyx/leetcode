from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mini = float('inf')
        prev = None

        def inorder(node):
            nonlocal mini, prev
            if node is None:
                return
            else:
                inorder(node.left)
                if prev is not None:
                    mini = min(mini, node.val - prev)
                prev = node.val
                inorder(node.right)

        inorder(root)
        return mini
    
s = Solution()

# root = [4, 2, 6, 1, 3]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(s.getMinimumDifference(root))