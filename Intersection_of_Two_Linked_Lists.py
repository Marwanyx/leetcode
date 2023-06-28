from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr = headA
        curr2 = headB

        while curr is not None:
            while curr2 is not None:
                if curr is curr2:
                    return curr2
                else:
                    curr2 = curr2.next
            curr = curr.next
            curr2 = headB

        return None
    
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr = headA
        curr2 = headB

        while curr is not None or curr2 is not None:
            if curr.val == curr2.val:
                if curr is curr2:
                    return curr
            

s = Solution()
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = headA.next.next

print(s.getIntersectionNode(headA, headB).val)