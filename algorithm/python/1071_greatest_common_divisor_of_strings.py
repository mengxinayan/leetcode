class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        while len2 != 0:
            tmp = len1 % len2
            len1 = len2
            len2 = tmp
        gcd_str1 = str1[:len1]
        gcd_str2 = str2[:len1]
        if gcd_str1 == gcd_str2:
            len_gcd_str = len(gcd_str1)
            if (str1 == gcd_str1 * (len(str1) // len_gcd_str)) and \
                (str2 == gcd_str1 * (len(str2) // len_gcd_str)):
                return gcd_str1
            else:
                return ''
        else:
            return ''

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
