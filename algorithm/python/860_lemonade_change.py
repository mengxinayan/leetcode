class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        now_change = {5:0, 10:0}
        ans = True
        for bill in bills:
            if bill == 5:
                now_change[bill] += 1
            elif bill == 10:
                if now_change[5] >= 1:
                    now_change[5] -= 1
                    now_change[bill] += 1
                else:
                    ans = False
                    break
            else:
                if (now_change[10] >= 1) and (now_change[5] >= 1):
                    now_change[10] -= 1
                    now_change[5] -= 1
                elif (now_change[5] >= 3):
                    now_change[5] -= 3
                else:
                    ans = False
                    break
        return ans

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
