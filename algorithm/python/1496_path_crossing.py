class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = [0, 0]
        visited = set()
        visited.add(tuple(curr))
        res = True
        for ch in path:
            if ch == 'N':
                curr[1] += 1
            elif ch == 'S':
                curr[1] -= 1
            elif ch == 'E':
                curr[0] += 1
            elif ch == 'W':
                curr[0] -= 1
            else:
                pass
            if tuple(curr) in visited:
                break
            else:
                visited.add(tuple(curr))
        else:
            res = False
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
