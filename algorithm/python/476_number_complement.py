class Solution:
    def findComplement(self, num: int) -> int:
        number = num
        valid_num = 31
        ans = 0
        while valid_num != 0:
            if (num & 0x80000000) == 0x80000000:
                break
            else:
                num = num << 1
                valid_num -= 1
        valid_number = valid_num
        while valid_num != 0:
            if (number & 0x1) == 0:
                ans += 2 ** (valid_number - valid_num)
            number = number >> 1
            valid_num -= 1
        return ans

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2022  mengxinayan

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
