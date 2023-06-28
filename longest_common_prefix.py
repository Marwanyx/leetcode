class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # solve
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        # find the shortest string
        shortest = strs[0]
        for i in range(1, len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]
        # find the longest common prefix
        prefix = ""
        for i in range(len(shortest)):
            for j in range(len(strs)):
                if shortest[i] != strs[j][i]:
                    return prefix
            prefix += shortest[i]
        return prefix
    
            

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))