class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        new = temp[::-1]
        
        return str(x) == new
    
s = Solution()
print(s.isPalindrome(121))