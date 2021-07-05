class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtracking(row: int, col: int, index: int) -> bool:
            if board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            else:
                visited[row][col] = 1
                ans = False
                for direction in direction_arr:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if (0 <= new_row < m) and (0 <= new_col < n) and (visited[new_row][new_col] == 0):
                        if backtracking(new_row, new_col, index+1) == True:
                            ans = True
                            break
                visited[row][col] = 0
                return ans

        first_letter_position = []
        m = len(board)
        n = len(board[0])
        direction_arr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[0 for j in range(n)] for i in range(m)]
        ans = False
        for i in range(m):
            for j in range(n):
                if backtracking(i, j, 0) == True:
                    ans = True
                    break
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
