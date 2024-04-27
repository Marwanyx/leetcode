class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(lambda:1)
        for num in nums:
            hashmap[num] += 1

        newdict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        newdict = list(newdict.keys())
        return newdict[:k]

