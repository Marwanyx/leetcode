from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        summ = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] - prices[j] < 0:
                    summ = max(abs(prices[i] - prices[j]), summ)

        return summ
    
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        min = 0
        for i in range(len(prices)):



s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 5