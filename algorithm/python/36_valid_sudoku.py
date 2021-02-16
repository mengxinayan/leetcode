class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True
        for i in range(9):
            tmp = set()
            for j in range(9):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res

        for i in range(9):
            tmp = set()
            for j in range(9):
                if board[j][i] in tmp:
                    res = False
                    break
                elif board[j][i].isdigit() == True:
                    tmp.add(board[j][i])
                else:
                    pass
        if res == False:
            return res

        tmp = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res

        tmp = set()
        for i in range(3):
            for j in range(3, 6):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res

        tmp = set()
        for i in range(3):
            for j in range(6, 9):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res
        
        tmp = set()
        for i in range(3, 6):
            for j in range(3):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res

        tmp = set()
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res

        tmp = set()
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res
        
        tmp = set()
        for i in range(6, 9):
            for j in range(3):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res

        tmp = set()
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res

        tmp = set()
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] in tmp:
                    res = False
                    break
                elif board[i][j].isdigit() == True:
                    tmp.add(board[i][j])
                else:
                    pass
        if res == False:
            return res
        
        return res

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
