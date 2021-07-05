class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        def is_win(player_moves: List[List[int]]) -> bool:
            # 0-2: row(top to bottom), 3-5: col(left to right)
            # 6: left top-right bottom, 7: right top-left bottom
            grid_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
            left_top_diagonal = {(0,0), (1,1), (2,2)}
            right_top_diagonal = {(0,2), (1,1), (2,0)}
            for move in player_moves:
                grid_dict[move[0]] += 1
                grid_dict[move[1]+3] += 1
                if tuple(move) in left_top_diagonal:
                    grid_dict[6] += 1
                if tuple(move) in right_top_diagonal:
                    grid_dict[7] += 1
            if 3 in grid_dict.values():
                return True
            else:
                return False

        if len(moves) < 5:
            return "Pending"
        A_moves = moves[0::2]
        B_moves = moves[1::2]
        if is_win(A_moves) == True:
            return "A"
        if is_win(B_moves) == True:
            return "B"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

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
