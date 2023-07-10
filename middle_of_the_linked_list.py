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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr = head
        slow = curr
        fast = curr.next

        if fast is None:
            return slow
        
        while fast is not None:
            if fast.next is None:
                return slow.next
            fast = fast.next.next
            slow = slow.next
        
        return slow
    

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(sol.middleNode(head))
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(sol.middleNode(head))