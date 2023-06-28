class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sApp = {}
        tApp = {}

        for i in range(len(s)):
            if s[i] in sApp:
                sApp[s[i]] += 1
            else:
                sApp[s[i]] = 1

        for j in range(len(t)):
            if t[j] in tApp:
                tApp[t[j]] += 1
            else:
                tApp[t[j]] = 1

        # sort the dictionary by key alphabetically
        sApp = sorted(sApp.items(), key=lambda x: x[0])
        tApp = sorted(tApp.items(), key=lambda x: x[0])

        if sApp == tApp:
            return True
        return False
        


s = Solution()
print(s.isAnagram("rat", "car"))