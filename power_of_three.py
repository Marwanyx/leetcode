class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0 and n > 0:
            n = n // 3
        
        return n == 1
    

s = Solution()
print(s.isPowerOfThree(10))