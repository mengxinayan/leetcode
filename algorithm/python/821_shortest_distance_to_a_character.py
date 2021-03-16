class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ch_index = []
        for i in range(len(S)):
            if S[i] == C:
                ch_index.append(i)
        ans = []
        count = 0
        for i in range(len(S)):
            if S[i] == C:
                ans.append(0)
                # 避免超出 ch_index 的索引范围
                # Avoid ch_index index out of range
                if count < len(ch_index) - 1:
                    count += 1
            else:
                ans.append(min(abs(i-ch_index[count]), abs(i-ch_index[count-1])))
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
