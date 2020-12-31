class Solution:
    def makeGood(self, s: str) -> str:
        # Use Stack
        res_ch = []
        for ch in s:
            if len(res_ch) == 0:
                res_ch.append(ch)
            else:
                if (res_ch[-1].islower() == True) and (res_ch[-1].upper() == ch):
                    res_ch.pop()
                elif (res_ch[-1].isupper() == True) and (res_ch[-1].lower() == ch):
                    res_ch.pop()
                else:
                    res_ch.append(ch)
        res = ''
        for ch in res_ch:
            res += ch
        return res

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
