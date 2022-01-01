class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def is_point_valid(a: int, b: int) -> bool:
            if (0 <= a < len(grid)) and (0 <= b < len(grid[0])):
                return True
            else:
                return False

        def check_and_add_land(a: int, b: int) -> int:
            if (is_point_valid(a, b) == True) and grid[a][b] == 1:
                tmp = str(a) + '-' + str(b)
                if tmp not in land_set:
                    land.append([a, b])
                    land_set.add(tmp)
                return 1
            else:
                return 0

        land = []
        land_set = set([])
        number_of_edge = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land.append([i, j])
                    tmp = str(i) + '-' + str(j)
                    land_set.add(tmp)
                    break
        i = 0
        while i != len(land):
            x = land[i][0]
            y = land[i][1]
            number_of_edge += check_and_add_land(x-1, y)
            number_of_edge += check_and_add_land(x+1, y)
            number_of_edge += check_and_add_land(x, y-1)
            number_of_edge += check_and_add_land(x, y+1)
            i += 1
        return i * 4 - number_of_edge

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
