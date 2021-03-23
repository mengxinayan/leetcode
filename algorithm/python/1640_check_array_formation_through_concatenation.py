class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        first_piece_dict = {}
        for piece in pieces:
            first_piece_dict[piece[0]] = piece
        i = 0
        ans = False
        while i != len(arr):
            if arr[i] in first_piece_dict:
                tmp = first_piece_dict[arr[i]]
                flag = False
                for j in range(len(tmp)):
                    if arr[i+j] != tmp[j]:
                        break
                else:
                    flag = True
                    del first_piece_dict[arr[i]]
                    i += len(tmp)
                if flag == False:
                    break
            else:
                break
        else:
            ans = True
        return ans

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
