class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        grid_sum = 0
        x = y = z = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid_sum += grid[i][j]
                if grid[i][j] > 1:
                    z += grid[i][j] - 1
                if i < len(grid) - 1:
                    x += min(grid[i][j], grid[i+1][j])
                if j < len(grid[0]) - 1:
                    y += min(grid[i][j], grid[i][j+1])
        return grid_sum*6 - (x+y+z)*2

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
