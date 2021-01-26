class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        len_num = {}
        for i in range(len(rectangles)):
            tmp = min(rectangles[i])
            if tmp not in len_num:
                len_num[tmp] = 1
            else:
                len_num[tmp] += 1
        max_len = max(len_num.keys())
        return len_num[max_len]

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
