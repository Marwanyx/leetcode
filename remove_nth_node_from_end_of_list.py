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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next is None:
            head = head.next
            return head
        
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        
        n = length - n

        curr = head
        i = 0

        if n == 0:
            head = head.next
            return head
        
        while curr is not None:
            if i + 1 == n:
                curr.next = curr.next.next
                return head
            i += 1
            curr = curr.next

s = Solution()
# 5, 
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(s.removeNthFromEnd(l1, 2))
l1 = ListNode(1, ListNode(2))
print(s.removeNthFromEnd(l1, 2))        
