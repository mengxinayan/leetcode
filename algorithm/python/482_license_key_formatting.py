class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper()
        tmp = ''
        for i in range(len(S)):
            if S[i] != '-':
                tmp += S[i]
        if len(tmp) == 0: # S = '---'
            return ''
        ans = ''
        first = len(tmp) % K
        i = 0
        if first != 0:
            ans += tmp[:first]
            i = first
        else:
            ans += tmp[:K]
            i = K
        while i != len(tmp):
            ans = ans + '-' + tmp[i:i+K]
            i += K
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
