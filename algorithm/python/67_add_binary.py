class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def bin_to_dec(s: str) -> int:
            res = 0
            nums = list(s)
            nums.reverse()
            for i in range(len(nums)):
                if nums[i] == '1':
                    res += 2**i
            return res

        def dec_to_bin(num: int) -> str:
            if num == 0:
                return '0'
            tmp = []
            while num != 0:
                tmp.append(num % 2)
                num = num // 2
            tmp.reverse() # 因为reverse方法没有返回值
            res = ''
            for i in range(len(tmp)):
                res += str(tmp[i])
            return res
        
        res = dec_to_bin(bin_to_dec(a) + bin_to_dec(b))
        return res