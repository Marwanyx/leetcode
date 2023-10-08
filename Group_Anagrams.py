from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        res = []
        keys = []
        flag = False
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            for j in range(len(keys)):
                if temp in keys[j]:
                    res[j].append(strs[i])
                    flag = True
            if not flag:
                res.append([strs[i]])
                keys.append([temp])
            flag = False

        return res

s = Solution()
print(s.groupAnagrams(["a"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["",""]))
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))