class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def bin_to_dec(s: str) -> int:
            ans = 0
            nums = list(s)
            nums.reverse()
            for i in range(len(nums)):
                if nums[i] == '1':
                    ans += 2**i
            return ans

        def dec_to_bin(num: int) -> str:
            if num == 0:
                return '0'
            tmp = []
            while num != 0:
                tmp.append(num % 2)
                num = num // 2
            tmp.reverse() # 因为reverse方法没有返回值
            ans = ''
            for i in range(len(tmp)):
                ans += str(tmp[i])
            return ans
        
        ans = dec_to_bin(bin_to_dec(a) + bin_to_dec(b))
        return ans

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020  mengxinayan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
