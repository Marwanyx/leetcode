from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head is None:
            return None
        
        curr = head
        while curr is not None and curr.val == val:
            head = head.next
            curr = head
        if curr is None:
            return None
        
        newHead = ListNode(curr.val)
        track = newHead
        curr = curr.next

        while curr is not None:
            if curr.val != val:
                track.next = ListNode(curr.val)
                track = track.next
            
            curr = curr.next

        return newHead
    

s = Solution()
# edge case, all elements are the same
head = ListNode(1, ListNode(1, ListNode(1, ListNode(1))))
val = 1
print(s.removeElements(head, val)) # None