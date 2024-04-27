from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for stri in strs:
            newStr = "".join(sorted(stri))
            if newStr in dct:
                dct[newStr].append(stri)
            else:
                dct[newStr] = [stri]
                
        return dct.values()