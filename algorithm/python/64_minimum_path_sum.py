class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if (i == 0) and (j == 0):
                    dp[i][j] = grid[i][j]
                elif (i == 0) and (j != 0):
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif (i != 0) and (j == 0):
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif (i != 0) and (j != 0):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                else:
                    pass
        return dp[m-1][n-1]

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
