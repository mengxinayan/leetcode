class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def is_self_dividing_number(number: int) -> bool:
            num = number
            res = True
            while num != 0:
                digit = num % 10
                if digit > 1:
                    if number % digit != 0:
                        res = False
                        break
                    else:
                        pass
                elif digit == 0:
                    res = False
                    break
                else:
                    pass
                num = num // 10
            return res
        
        res = []
        for i in range(left, right+1):
            if is_self_dividing_number(i) == True:
                res.append(i)
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
