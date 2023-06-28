class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1

        while i**2 < x:
            i += 1
            
        if i**2 > x:
            return i - 1
        return i
    

s = Solution()
print(s.mySqrt(8))