from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []

        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        
        return lst == lst[::-1]
    
s = Solution()
print(s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
print(s.isPalindrome(ListNode(1, ListNode(2))))