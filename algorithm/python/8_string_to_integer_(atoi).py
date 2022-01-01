class Solution:
    def myAtoi(self, s: str) -> int:
        num_str = ''
        flag = True
        for ch in s:
            if (ch == '-') or (ch == '+'):
                if flag == True:
                    num_str += ch
                    flag = False
                else:
                    break
            elif ch == ' ':
                if flag == True:
                    num_str += ch
                else:
                    break
            elif ch.isdigit() == True:
                num_str += ch
                flag = False
            else:
                break
        num_str = num_str.strip(' ')
        if (num_str == '') or (num_str == '+') or (num_str == '-'):
            return 0
        num = int(num_str)
        max_range = 2 ** 31
        if num < -max_range:
            return -max_range
        if num > max_range - 1:
            return max_range - 1
        return num

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
