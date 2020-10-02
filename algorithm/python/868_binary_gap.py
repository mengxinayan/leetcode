class Solution:
    def binaryGap(self, n: int) -> int:
        count = 0
        index_arr = []
        while n != 0:
            if n % 2 == 1:
                index_arr.append(count)
            count += 1
            n //= 2
        if len(index_arr) <= 1:
            return 0
        res = -1
        for i in range(1, len(index_arr)):
            res = max(res, index_arr[i] - index_arr[i-1])
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
