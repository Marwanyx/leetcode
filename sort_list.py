from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = []
        curr = head
        while curr is not None:
            nodes.append(curr.val)
            curr = curr.next

        nodes.sort()

        newLL = ListNode(nodes[0])
        curr = newLL

        for val in nodes[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return newLL