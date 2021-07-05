# Solution 1

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:

        def cal_bits_number(num: int):
            ans = 0
            while num != 0:
                if num % 2 == 1:
                    ans += 1
                num = num // 2
            return ans
        
        prime_number_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        ans = 0
        for i in range(L, R+1):
            if cal_bits_number(i) in prime_number_set:
                ans += 1
        return ans


# Solution 2

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int: 
        prime_number_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        ans = 0
        for i in range(L, R+1):
            if (bin(i).count('1')) in prime_number_set:
                ans += 1
        return ans

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2021  mengxinayan

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
