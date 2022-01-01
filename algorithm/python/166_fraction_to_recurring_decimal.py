class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        ans = []
        if numerator / denominator < 0:
            ans.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        quotient = numerator // denominator
        remainder = numerator % denominator
        ans.append(str(quotient))
        if remainder != 0:
            ans.append('.')
            remainder_dic = {}
            while remainder != 0:
                if remainder in remainder_dic:
                    ans.insert(remainder_dic[remainder], '(')
                    ans.append(')')
                    break
                
                remainder_dic[remainder] = len(ans)
                remainder *= 10
                ans.append(str(remainder // denominator))
                remainder = remainder % denominator
        return ''.join(ans)

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
