class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if (obstacleGrid[0][0] == 1) or (obstacleGrid[m-1][n-1] == 1):
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if (i==0) and (j==0) and (obstacleGrid[i][j] == 0):
                        dp[i][j] = 1
                    elif (i == 0) and (j != 0) and (obstacleGrid[i][j] == 0):
                        dp[i][j] = dp[i][j-1]
                    elif (i != 0) and (j == 0) and (obstacleGrid[i][j] == 0):
                        dp[i][j] = dp[i-1][j]
                    elif (i != 0) and (j != 0) and (obstacleGrid[i][j] == 0):
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    else:
                        pass
        return dp[m-1][n-1]

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
