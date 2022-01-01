class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = []
        for row in matrix:
            row_min.append(min(row))
        col_max = []
        for i in range(len(matrix[0])):
            col = [matrix[j][i] for j in range(len(matrix))]
            col_max.append(max(col))
        ans = []
        for i in range(len(row_min)):
            for j in range(len(col_max)):
                if row_min[i] == col_max[j]:
                    ans.append(matrix[i][j])
        return ans

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
