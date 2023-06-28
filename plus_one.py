from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                if digits[i - 1] == 9:
                    continue
                else:
                    if i == 0:
                        digits.insert(0, 1)
                        return digits
                    digits[i - 1] += 1
                    return digits
            else:
                digits[i] += 1
                return digits

class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        new = "".join(digits)
        new = int(new) + 1
        return [int(i) for i in str(new)]


s = Solution()
print(s.plusOne([9, 9, 9, 9]))

s2 = Solution2()
print(s2.plusOne([9, 9, 9, 9]))