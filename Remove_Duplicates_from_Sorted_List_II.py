from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashMap = {}

        if head is None:
            return None
        curr = head

        while curr is not None:
            if curr.val not in hashMap:
                hashMap[curr.val] = 1
            elif curr.val in hashMap:
                hashMap[curr.val] += 1

            curr = curr.next

        values = []
        for key, val in hashMap.items():
            if val == 1:
                values.append(key)

        if len(values) == 0:
            return None
        
        newLL = ListNode(values[0])
        track = newLL
        for val in values[1:]:
            track.next = ListNode(val)
            track = track.next

        return newLL
    

s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
print(s.deleteDuplicates(head)) # 1 -> 2 -> 5

head = ListNode(1, ListNode(1))
print(s.deleteDuplicates(head)) # None

