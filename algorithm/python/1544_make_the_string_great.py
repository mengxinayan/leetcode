class Solution:
    def makeGood(self, s: str) -> str:
        # Use Stack
        ans_ch = []
        for ch in s:
            if len(ans_ch) == 0:
                ans_ch.append(ch)
            else:
                if (ans_ch[-1].islower() == True) and (ans_ch[-1].upper() == ch):
                    ans_ch.pop()
                elif (ans_ch[-1].isupper() == True) and (ans_ch[-1].lower() == ch):
                    ans_ch.pop()
                else:
                    ans_ch.append(ch)
        ans = ''
        for ch in ans_ch:
            ans += ch
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
