class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            curr = s2[l:r + 1]
            if len(curr) == len(s1):
                if sorted(curr) == sorted(s1):
                    return True
            l += 1
            r += 1
            
        return False

s = Solution()

s1 = "hello"
s2 = "ooolleoooleh"

print(s.checkInclusion(s1, s2))  # Expected: False