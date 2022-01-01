class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_start = odd_end = 0
        if low % 2 == 1:
            odd_start = low
        else:
            odd_start = low + 1
        if high % 2 == 1:
            odd_end = high
        else:
            odd_end = high - 1
        return (odd_end - odd_start) // 2 + 1

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
