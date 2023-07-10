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
        num1 = []
        num2 = []

        curr = l1
        while curr is not None:
            num1.insert(0, curr.val)
            curr = curr.next

        curr = l2
        while curr is not None:
            num2.insert(0, curr.val)
            curr = curr.next

        number1 = int(''.join(map(str, num1)))
        number2 = int(''.join(map(str, num2)))

        summ = number1 + number2
        sum = list(map(int, str(summ)))

        ll = ListNode(sum.pop())
        curr = ll
        # reversed loop
        for i in reversed(range(len(sum))):
            curr.next = ListNode(sum[i])
            curr = curr.next

        return ll

s = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(s.addTwoNumbers(l1, l2))
l1 = ListNode(0)
l2 = ListNode(0)
print(s.addTwoNumbers(l1, l2))


        