class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        def divide_value(dividend_value: int, divisor_value: int) -> int:
            if dividend_value == 0:
                return 0
            if dividend_value < divisor_value:
                return 0
            count = 1
            tmp = divisor_value
            while tmp + tmp <= dividend_value:
                count += count
                tmp += tmp
            return count +divide_value(dividend_value-tmp, divisor_value)

        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == -2147483648:
                return 2147483647
            else:
                return -dividend
        sign = -1
        if ((dividend > 0) and (divisor > 0)) or ((dividend < 0) and (divisor < 0)):
            sign = 1
        dividend_value = abs(dividend)
        divisor_value = abs(divisor)
        quotient_value = divide_value(dividend_value, divisor_value)
        return quotient_value * sign

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2021  mengxinayan

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
