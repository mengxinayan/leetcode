class Solution:
    def countLargestGroup(self, n: int) -> int:

        def sum_of_num(num: int) -> int:
            res = 0
            while num != 0:
                res += num % 10
                num //= 10
            return res
        
        sum_num_dict = {}
        for num in range(1, n+1):
            tmp = sum_of_num(num)
            if tmp not in sum_num_dict:
                sum_num_dict[tmp] = 1
            else:
                sum_num_dict[tmp] += 1
        max_sum_num = max(list(sum_num_dict.values()))
        res = 0
        for key in sum_num_dict:
            if sum_num_dict[key] == max_sum_num:
                res += 1
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
