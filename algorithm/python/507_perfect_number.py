class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 4:
            return False
        divisors = []
        length = int(math.sqrt(num)) + 1
        for i in range(2, length):
            if num % i == 0:
                if num / i == i:
                    divisors.append(i)
                else:
                    divisors.append(i)
                    divisors.append(num/i)
        divisors_sum = 1 + sum(divisors) # Because 1 must be a factor
        if divisors_sum == num:
            return True
        else:
            return False

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
