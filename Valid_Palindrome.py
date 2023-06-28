class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in range(len(s)):
            if s[i].isalnum():
                result += s[i]
        s = result.lower()
        
        return s == s[::-1]
    
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))