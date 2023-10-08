class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()

        return len(temp[-1])
    
s = Solution()
s.lengthOfLastWord("   fly me   to   the moon  ")