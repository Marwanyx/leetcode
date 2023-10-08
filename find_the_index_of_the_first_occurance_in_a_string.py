class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack or not needle:
            return -1

        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+l] == needle:
                return i
            
            
s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "leeto"))
print(s.strStr("", ""))
print(s.strStr("hello", "ll"))

