from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        head = ListNode(head.val)
        track = head
        app = [head.val]
        while curr is not None:
            if curr.val not in app:
                app.append(curr.val)
                track.next = ListNode(curr.val)
                track = track.next
            
            curr = curr.next

        return head
    
s = Solution()
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
head = s.deleteDuplicates(head)

while head is not None:
    print(head.val)
    head = head.next



