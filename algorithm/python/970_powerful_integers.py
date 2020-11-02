class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if (x == 1) and (y == 1):
            if bound >= 2:
                return [2]
            else:
                return []
        elif (x == 1) and (y != 1):
            res_set = set()
            j = 0
            tmp = x + y**j
            while tmp <= bound:
                res_set.add(tmp)
                j += 1
                tmp = x + y**j
            return list(res_set)
        elif (x != 1) and (y == 1):
            res_set = set()
            i = 0
            tmp = x**i + y
            while tmp <= bound:
                res_set.add(tmp)
                i += 1
                tmp = x**i + y
            return list(res_set)
        else:
            res_set = set()
            i = j = 0
            tmp = x**i + y**j
            while tmp <= bound:
                while tmp <= bound:
                    res_set.add(tmp)
                    j += 1
                    tmp = x**i + y**j
                i += 1
                j = 0
                tmp = x**i + y**j
            return list(res_set)

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
