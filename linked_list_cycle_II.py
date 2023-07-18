from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        app = []
        curr = head

        while curr is not None:
            if curr not in app:
                app.append(curr)
            else:
                return curr
            
            curr = curr.next
        
        return None