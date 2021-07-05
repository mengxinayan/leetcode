class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 4:
            if (num == 1) or (num == 4):
                return True
            else:
                return False
        else:
            ans = True
            left = 0
            right = num
            mid = (left + right) // 2
            while 1:
                if mid * mid == num:
                    break
                elif mid * mid > num:
                    if (mid-1) * (mid-1) == num:
                        break
                    elif (mid-1) * (mid-1) < num:
                        ans = False
                        break
                    else:
                        right = mid - 1
                        mid = (left + right) // 2
                else:
                    if (mid+1) * (mid+1) == num:
                        break
                    elif (mid+1) * (mid+1) > num:
                        ans = False
                        break
                    else:
                        left = mid + 1
                        mid = (left + right) // 2
            return ans

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
