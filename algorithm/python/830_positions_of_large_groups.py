class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = 0
        count = 1
        ch = s[0]
        ans = []
        for i in range(1, len(s)):
            if s[i] == ch:
                count += 1
            else:
                if count >= 3:
                    ans.append([start, i-1])
                start = i
                ch = s[i]
                count = 1
        # 字符串末尾的字符符合条件，例如："abbb"
        # The characters at the end of the string meet the conditions, for example: "abbb"
        if count >= 3:
            ans.append([start, len(s)-1])
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
