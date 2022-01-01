class Solution:
    def reformat(self, s: str) -> str:

        def reformat_0(str1: str, str2: str) -> str:
            # len(str1) == len(str2)
            ans = ''
            for i in range(len(str1)):
                ans += str1[i] + str2[i]
            return ans

        def reformat_1(str1: str, str2: str) -> str:
            # len(str1) == len(str2) + 1
            ans = ''
            for i in range(len(str2)):
                ans += str1[i] + str2[i]
            ans += str1[-1]
            return ans

        chars = []
        digits = []
        for ch in s:
            if ch.isalpha() == True:
                chars.append(ch)
            else:
                digits.append(ch)
        if abs(len(chars) - len(digits)) <= 1:
            if len(chars) == len(digits) + 1:
                return reformat_1(chars, digits)
            elif len(digits) == len(chars) + 1:
                return reformat_1(digits, chars)
            else:
                return reformat_0(chars, digits)
        else:
            return ""

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
