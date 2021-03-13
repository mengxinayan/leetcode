class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if (len(g) == 0) or (len(s) == 0):
            return 0
        g.sort()
        g.reverse()
        s.sort()
        s.reverse()
        ans = 0
        i = j = 0
        while (i != len(s)) and (j != len(g)):
            if s[i] >= g[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
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
