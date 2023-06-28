class Solution:
    def isHappy(self, n: int) -> bool:
        total = n
        while total != 1:
            num = [int(a) for a in str(total)]
            total = 0
            for i in range(len(num)):
                summ = (num[i])**2
                total += summ
            if total == n:
                return False
                
        return True
        

s = Solution()
print(s.isHappy(2))