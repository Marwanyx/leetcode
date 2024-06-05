from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dct = {}
        for word in words:
            if word not in dct:
                dct[word] = 1
            else:
                dct[word] += 1
        
        lst = sorted(dct.items(), key=lambda x: (-x[1], x[0]))
        return [lst[i][0] for i in range(k)]
        
            

s = Solution()

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(s.topKFrequent(words, k)) # ["i", "love"]