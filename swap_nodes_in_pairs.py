from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"
    
    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        curr = head

        while curr is not None:
            first = curr
            second = curr.next
            if second is None:
                return head
            first.val, second.val = second.val, first.val
            curr = curr.next.next

        return head
    

s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(s.swapPairs(head))
head = None
print(s.swapPairs(head))
head = ListNode(1, ListNode(2, ListNode(3)))
print(s.swapPairs(head))