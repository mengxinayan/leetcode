class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        group_len = numRows * 2 - 2
        ch_group = {}
        for i in range(group_len):
            ch_group[i] = []
        for i in range(len(s)):
            ch_group[i%group_len].append(s[i])
        ans = ''
        for i in range(group_len//2+1):
            if i == 0:
                for ch in ch_group[i]:
                    ans += ch
            elif i == group_len//2:
                for ch in ch_group[i]:
                    ans += ch
            else:
                j = group_len - i
                m = n = 0
                group_i_len = len(ch_group[i])
                group_j_len = len(ch_group[j])
                while (m < group_i_len) or (n < group_j_len):
                    if m < group_i_len:
                        ans += ch_group[i][m]
                        m += 1
                    if n < group_j_len:
                        ans += ch_group[j][n]
                        n += 1
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
