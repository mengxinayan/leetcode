class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for ch in ops:
            if ch == '+':
                arr.append(arr[len(arr)-1] + arr[len(arr)-2])
            elif ch == 'D':
                arr.append(arr[len(arr)-1]*2)
            elif ch == 'C':
                arr.pop()
            else:
                arr.append(int(ch))
        return sum(arr)

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
