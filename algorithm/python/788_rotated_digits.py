class Solution:
    def rotatedDigits(self, N: int) -> int:

        def is_good(num: int) -> bool:
            string = str(num)
            if ('3' in string) or ('4' in string) or ('7' in string):
                return False
            if ('2' in string) or ('5' in string) or ('6' in string) or ('9' in string):
                return True
            return False

        ans = 0
        for i in range(1, N+1):
            if is_good(i) == True:
                ans += 1
        return ans

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
