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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        i = 0
        curr = head
        first = head
        before_last = head
        prev = None

        nodes = []
        while curr is not None:
            nodes.append(curr)
            curr = curr.next

        if len(nodes) == 1:
            return head
        elif len(nodes) == 2 and k == 0:
            return head
        
        before_last = nodes[-2]
        last = nodes[-1]

        while i != k:
            before_last = nodes[-2]
            last = nodes[-1]
            before_last.next = None
            last.next = first
            first = last
            i += 1
            n = nodes.pop()
            nodes.insert(0, n)

        return last
    
s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(s.rotateRight(head, 2))
head = ListNode(0, ListNode(1, ListNode(2)))
print(s.rotateRight(head, 4))
head = ListNode(1, ListNode(2))
print(s.rotateRight(head, 1))

