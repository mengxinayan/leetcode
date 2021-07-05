class Solution:
    def judgeCircle(self, moves: str) -> bool:
        end_X = end_Y = 0
        for ch in moves:
            if ch == 'U':
                end_Y += 1
            elif ch == 'D':
                end_Y -= 1
            elif ch == 'R':
                end_X += 1
            else:
                end_X -= 1
        if (end_X == 0) and (end_Y == 0):
            return True
        else:
            return False

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
