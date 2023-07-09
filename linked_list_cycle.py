from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        app = []
        curr = head

        while curr is not None:
            if curr not in app:
                app.append(curr)
            else:
                return True
            
            curr = curr.next
        
        return False
    
s = Solution()
s.hasCycle(ListNode(3))