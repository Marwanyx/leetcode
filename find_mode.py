from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dct = {}

        def inorder(node):
            if node is None:
                return
            else:
                inorder(node.left)
                if node.val in dct:
                    dct[node.val] += 1
                else:
                    dct[node.val] = 1
                inorder(node.right)

        inorder(root)
        max_freq = max(dct.values())

        return [k for k, v in dct.items() if v == max_freq]
    



s = Solution()

# root = [1, None, 2, 2]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

print(s.findMode(root))