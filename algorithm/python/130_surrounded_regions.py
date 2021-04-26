class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def cal_adjacent_node(node: List[int]) -> None:
            if tuple(node) not in node_set:
                node_set.add(tuple(node))
                for direct in direct_arr:
                    new_i = node[0] + direct[0]
                    new_j = node[1] + direct[1]
                    if (0 <= new_i < row) and (0 <= new_j < col) and (board[new_i][new_j] == 'O'):
                        cal_adjacent_node([new_i, new_j])

        row = len(board)
        col = len(board[0])
        start_node = []
        for i in range(row):
            if board[i][0] == 'O':
                start_node.append([i, 0])
            if board[i][col-1] == 'O':
                start_node.append([i, col-1])
        for j in range(col):
            if board[0][j] == 'O':
                start_node.append([0, j])
            if board[row-1][j] == 'O':
                start_node.append([row-1, j])
        node_set = set()
        direct_arr = [[0,1], [0,-1], [1,0], [-1,0]]
        for tmp_node in start_node:
            cal_adjacent_node(tmp_node)
        for i in range(row):
            for j in range(col):
                if (board[i][j] == 'O') and (tuple([i, j]) not in node_set):
                    board[i][j] = 'X'

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
