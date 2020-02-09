class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        tmp = 5
        while n >= tmp:
            res += (n // tmp)
            tmp *= 5
        return res