from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                newNode = ListNode(list1.val, ListNode(list2.val))
            else:
                newNode = ListNode(list2.val, ListNode(list1.val))
        head = newNode
        track = newNode.next
        curr1 = list1.next
        curr2 = list2.next
        while curr1 is not None:
            if curr1.val < curr2.val:
                track.next = ListNode(curr1.val, ListNode(curr2.val))
            else:
                track.next = ListNode(curr2.val, ListNode(curr1.val))

            curr1 = curr1.next
            curr2 = curr2.next
            track = track.next.next
        
        return head
    
s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
print(s.mergeTwoLists(list1, list2))