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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return None
        
        curr = l1
        num1 = ''
        while curr is not None:
            num1 += str(curr.val)
            curr = curr.next

        curr = l2
        num2 = ''
        while curr is not None:
            num2 += str(curr.val)
            curr = curr.next

        if num1 == '':
            num1 = '0'
        elif num2 == '':
            num2 = '0'

        num1 = int(num1)
        num2 = int(num2)
        total = num1 + num2
        total = str(total)

        ll = ListNode(int(total[0]))
        curr = ll

        for num in total[1:]:
            curr.next = ListNode(int(num))
            curr = curr.next

        return ll


s = Solution()
l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(s.addTwoNumbers(l1, l2))
