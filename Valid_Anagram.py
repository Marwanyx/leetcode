class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sL = sorted(s)
        tL = sorted(t)

        return sL == tL