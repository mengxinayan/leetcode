class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_freq = {}
        for num in arr:
            if num not in num_freq:
                num_freq[num] = 1
            else:
                num_freq[num] += 1
        res_list = []
        for num in num_freq:
            if num_freq[num] == num:
                res_list.append(num)
        if len(res_list) == 0:
            return -1
        else:
            return max(res_list)

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
