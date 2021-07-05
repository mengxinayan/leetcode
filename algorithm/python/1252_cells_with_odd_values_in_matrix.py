class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        def add_one_row(arr: List[List[int]], row: int):
            for i in range(len(arr[0])):
                arr[row][i] += 1

        def add_one_col(arr: List[List[int]], col: int):
            for i in range(len(arr)):
                arr[i][col] += 1
        
        arr = [[0 for i in range(m)] for j in range(n)]
        for index in indices:
            add_one_row(arr, index[0])
            add_one_col(arr, index[1])
        ans = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] % 2 == 1:
                    ans += 1
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
