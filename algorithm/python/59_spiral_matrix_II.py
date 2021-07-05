class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)] for j in range(n)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        current_direction = i = j = 0
        for num in range(1, n*n+1):
            ans[i][j] = num
            next_i = i + direction[current_direction][0]
            next_j = j + direction[current_direction][1]
            if (0 <= next_i < n) and (0 <= next_j < n) and (ans[next_i][next_j] == 0):
                i = next_i
                j = next_j
            else:
                current_direction = (current_direction + 1) % 4
                i += direction[current_direction][0]
                j += direction[current_direction][1]
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
