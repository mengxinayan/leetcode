class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def dfs_fill(x: int, y: int):
            image[x][y] = newColor
            for m, n in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                if (0 <= m < len(image)) and (0 <= n < len(image[m])) and (image[m][n] == self.original_color):
                    dfs_fill(m, n)

        self.original_color = image[sr][sc]
        if self.original_color != newColor:
            dfs_fill(sr, sc)
        return image

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
