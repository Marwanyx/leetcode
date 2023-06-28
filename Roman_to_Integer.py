class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1:
                if s[i] == "I" and s[i + 1] == "V":
                    total += 4
                    i += 1
                elif s[i] == "I" and s[i + 1] == "X":
                    total += 9
                    i += 1
                elif s[i] == "X" and s[i + 1] == "L":
                    total += 40
                    i += 1
                elif s[i] == "X" and s[i + 1] == "C":
                    total += 90
                    i += 1
                elif s[i] == "C" and s[i + 1] == "D":
                    total += 400
                    i += 1
                elif s[i] == "C" and s[i + 1] == "M":
                    total += 900
                    i += 1
                else:
                    total += dct[s[i]]
                    
            else:
                total += dct[s[i]]
            i += 1
        
        return total
    
s = Solution()
print(s.romanToInt("MCMXCIV"))