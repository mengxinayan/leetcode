class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        Bi = Bj = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    Bi = i
                    Bj = j
                    break
        ans = 0
        j = Bj - 1
        while j >= 0:
            if board[Bi][j] == 'p':
                ans += 1
                break
            elif board[Bi][j] == 'B':
                break
            else:
                j -= 1
        j = Bj + 1
        while j <= 7:
            if board[Bi][j] == 'p':
                ans += 1
                break
            elif board[Bi][j] == 'B':
                break
            else:
                j += 1
        i = Bi - 1
        while i >= 0:
            if board[i][Bj] == 'p':
                ans += 1
                break
            elif board[i][Bj] == 'B':
                break
            else:
                i -= 1
        i = Bi + 1
        while i <= 7:
            if board[i][Bj] == 'p':
                ans += 1
                break
            elif board[i][Bj] == 'B':
                break
            else:
                i += 1
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
