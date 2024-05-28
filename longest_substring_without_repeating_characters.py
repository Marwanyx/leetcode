class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1

            cSet.add(s[r])
            result = max(result, r - l + 1)

        return result
    

s = Solution()

# Test case 1
st = "abbbbb"
print(s.lengthOfLongestSubstring(st))  # Expected: 2