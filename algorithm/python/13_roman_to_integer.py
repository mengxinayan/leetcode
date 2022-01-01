class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        i = 0
        while (i != len(s)):
            if s[i] == 'I':
                if i+1 != len(s) and s[i+1] == 'V':
                    ans += 4
                    i += 1
                elif i+1 != len(s) and s[i+1] == 'X':
                    ans += 9
                    i += 1
                else:
                    ans += 1
            elif s[i] == 'V':
                ans += 5
            elif s[i] == 'X':
                if i+1 != len(s) and s[i+1] == 'L':
                    ans += 40
                    i += 1
                elif i+1 != len(s) and s[i+1] == 'C':
                    ans += 90
                    i += 1
                else:
                    ans += 10
            elif s[i] == 'L':
                ans += 50
            elif s[i] == 'C':
                if i+1 != len(s) and s[i+1] == 'D':
                    ans += 400
                    i += 1
                elif i+1 != len(s) and s[i+1] == 'M':
                    ans += 900
                    i += 1
                else:
                    ans += 100
            elif s[i] == 'D':
                ans += 500
            else:
                ans += 1000
            i += 1
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
