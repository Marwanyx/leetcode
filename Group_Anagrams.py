from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        result = []
        minRes = []

        for word in strs:
            char = []
            for letter in word:
                char.append(letter)
            char.sort()
            map[word] = char

        # "eat": ["a", "e", "t"]
        # "tea": ["a", "e", "t"]
        nextMap = dict(map)
        while map != {}:
            minRes = []
            nextMap = {}
            temp = list(map.values())
            val = temp[0]
            for words in map:
                if map[words] == val:
                    minRes.append(words)
                else:
                    nextMap[words] = map[words]
            map = dict(nextMap)
                    
            result.append(minRes)

        return result
    

s = Solution()
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["",""]))
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))