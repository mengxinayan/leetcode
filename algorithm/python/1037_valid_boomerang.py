class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = (points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2
        b = (points[0][0] - points[2][0]) ** 2 + (points[0][1] - points[2][1]) ** 2
        c = (points[1][0] - points[2][0]) ** 2 + (points[1][1] - points[2][1]) ** 2
        arr = [a, b, c]
        max_num = max(arr)
        min_num = min(arr)
        arr.remove(max_num)
        arr.remove(min_num)
        mid_num = arr[0]
        if math.sqrt(max_num) < math.sqrt(mid_num) + math.sqrt(min_num):
            return True
        else:
            return False

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
