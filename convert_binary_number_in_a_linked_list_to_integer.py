# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []

        curr = head
        while curr is not None:
            binary.append(str(curr.val))
            curr = curr.next

        bina = ''.join(binary)
        bina = int(bina, 2)
        return bina

s = Solution
head = ListNode(1, ListNode(0, ListNode(1)))
print(s.getDecimalValue(s, head))