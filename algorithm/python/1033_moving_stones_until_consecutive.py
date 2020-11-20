class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        num_set = {a, b, c}
        x = min(a, b, c)
        z = max(a, b, c)
        num_set.remove(x)
        num_set.remove(z)
        y = list(num_set)[0]
        left_diff = y-x
        right_diff = z-y
        min_moves = max_moves = -1
        if (left_diff == 1) and (right_diff == 1):
            return [0, 0]
        elif (left_diff == 1) or (left_diff == 2) or (right_diff == 1) or (right_diff == 2):
            min_moves = 1
        else:
            min_moves = 2
        max_moves = left_diff + right_diff - 2
        return [min_moves, max_moves]

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
