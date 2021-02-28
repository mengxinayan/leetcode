class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        def number_sum(num: int) -> int:
            res = 0
            while num != 0:
                res += num % 10
                num //= 10
            return res
        
        tmp = [0 for i in range(50)]
        for i in range(lowLimit, highLimit+1):
            index = number_sum(i)
            tmp[index] += 1
        return max(tmp)

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
