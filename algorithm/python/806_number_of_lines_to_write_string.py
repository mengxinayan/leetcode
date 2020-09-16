class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if S == '':
            return [0, 0]
        lines = 1
        res = 0
        for ch in S:
            res += widths[ord(ch)-ord('a')]
            if res > 100:
                res = widths[ord(ch)-ord('a')]
                lines += 1
        return [lines, res]

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
