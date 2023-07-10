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

        hashSet = set()

        while curr is not None:
            hashSet.add(curr)
            curr = curr.next

        curr = headB
        while curr is not None:
            if curr in hashSet:
                return curr
            curr = curr.next

        return None
    

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