class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1 or x == 2 or x == 3:
            return 1
        else:
            res = 0
            left = 0
            right = x
            mid = (left + right) // 2
            while (1):
                if mid * mid == x:
                    res = mid
                    break
                elif mid * mid > x:
                    if (mid-1) * (mid-1) <= x:
                        res = mid - 1
                        break
                    else:
                        right = mid - 1
                        mid = (left + right) // 2
                else:
                    if (mid+1) * (mid+1) > x:
                        res = mid
                        break
                    elif (mid+1) * (mid+1) == x:
                        res = mid + 1
                        break
                    else:
                        left = mid + 1
                        mid = (left + right) // 2
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