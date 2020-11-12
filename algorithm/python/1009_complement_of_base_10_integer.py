class Solution:
    def bitwiseComplement(self, N: int) -> int:
        num = 1
        while num < N:
            # 移位的优先级比加法低
            # Shifting takes a lower priority than addition
            num = (num << 1) + 1
        return N ^ num
