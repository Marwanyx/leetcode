from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
    
s = Solution()
lst = ["h","e","l","l","o"]
s.reverseString(lst)
print(lst) # ["o","l","l","e","h"]