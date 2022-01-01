class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

        def process_M(M: List[List[int]]) -> List[List[int]]:
            ans = copy.deepcopy(M)
            for i in range(len(M)):
                ans[i].append(0)
                ans[i].insert(0, 0)
            ans.insert(0, [0 for i in range(len(M[0])+2)])
            ans.append([0 for i in range(len(M[0])+2)])
            return ans
        
        def cal_surrounding_cells_sum(M: List[List[int]], i, j) -> int:
            return M[i-1][j-1] + M[i-1][j] + M[i-1][j+1] + M[i][j-1] + M[i][j] + M[i][j+1] + M[i+1][j-1] + M[i+1][j] + M[i+1][j+1]

        matrix_row = len(M)
        matrix_col = len(M[0])
        if (matrix_row == 1) and (matrix_col == 1):
            return M
        if (matrix_row == 1) or (matrix_col == 1):
            if matrix_row == 1:
                ans = [[0 for i in range(matrix_col)]]
                ans[0][0] = (M[0][0] + M[0][1]) // 2
                ans[0][matrix_col-1] = (M[0][matrix_col-1] + M[0][matrix_col-2]) // 2
                for i in range(1, matrix_col-1):
                    ans[0][i] = (M[0][i-1] + M[0][i] + M[0][i+1]) // 3
                return ans
            else:
                ans = [[0] for i in range(matrix_row)]
                ans[0][0] = (M[0][0] + M[1][0]) // 2
                ans[matrix_row-1][0] = (M[matrix_row-1][0] + M[matrix_row-2][0]) // 2
                for i in range(1, matrix_row-1):
                    ans[i][0] = (M[i-1][0] + M[i][0] + M[i+1][0]) // 3
                return ans

        new_M = process_M(M)
        matrix_angles = [[0,0], [0, matrix_col-1], [matrix_row-1, 0], [matrix_row-1, matrix_col-1]]
        matrix_row_edge_set = set([i for i in range(1, matrix_row)])
        matrix_col_edge_set = set([i for i in range(1, matrix_col)])
        ans = [[0 for i in range(matrix_col)] for j in range(matrix_row)]
        for i in range(matrix_row):
            for j in range(matrix_col):
                if [i, j] in matrix_angles:
                    ans[i][j] = cal_surrounding_cells_sum(new_M, i+1, j+1)//4
                elif ( (i in {0, matrix_row-1}) and (j in matrix_col_edge_set) ) \
                  or ( (j in {0, matrix_col-1}) and (i in matrix_row_edge_set) ):
                    ans[i][j] = cal_surrounding_cells_sum(new_M, i+1, j+1)//6
                else:
                    ans[i][j] = cal_surrounding_cells_sum(new_M, i+1, j+1)//9
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
