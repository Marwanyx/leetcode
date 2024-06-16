class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        x = str(x)
        if x[0] == "-":
            # reverse except the negative sign
            x = x[1:][::-1]
            res = int("-" + x)
        else:
            res = int(x[::-1])

        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
        
s = Solution()
print(s.reverse(123)) # Expected output: 321

print(s.reverse(-123)) # Expected output: -321

print(s.reverse(120)) # Expected output: 21