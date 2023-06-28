class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystackList = list(haystack)
        needleList = list(needle)
        index = -1
        for i in range(len(haystackList)):
            if haystackList[i] == needleList[i]:
                index = i
                for j in range(i, len(needleList)):
                    if haystackList[j] == needleList[j]:
                        continue
                    else:
                        break
        
        return -1
    
s = Solution()
haystack = "leetcode"
needle = "leeto"
print(s.strStr(haystack, needle))