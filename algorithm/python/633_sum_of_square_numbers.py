class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 4:
            if c != 3:
                return True
            else:
                return False
        else:
            square_nums = []
            max_num = int(math.sqrt(c)) + 1
            for i in range(max_num):
                square_nums.append(i**2)
            square_nums_set = set(square_nums)
            res = False
            for i in range(len(square_nums)):
                if c-square_nums[i] in square_nums_set:
                    res = True
                    break
                else:
                    pass
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
