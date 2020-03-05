class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        while (i != len(s)):
            if s[i] == 'I':
                if i+1 != len(s) and s[i+1] == 'V':
                    res += 4
                    i += 1
                elif i+1 != len(s) and s[i+1] == 'X':
                    res += 9
                    i += 1
                else:
                    res += 1
            elif s[i] == 'V':
                res += 5
            elif s[i] == 'X':
                if i+1 != len(s) and s[i+1] == 'L':
                    res += 40
                    i += 1
                elif i+1 != len(s) and s[i+1] == 'C':
                    res += 90
                    i += 1
                else:
                    res += 10
            elif s[i] == 'L':
                res += 50
            elif s[i] == 'C':
                if i+1 != len(s) and s[i+1] == 'D':
                    res += 400
                    i += 1
                elif i+1 != len(s) and s[i+1] == 'M':
                    res += 900
                    i += 1
                else:
                    res += 100
            elif s[i] == 'D':
                res += 500
            else:
                res += 1000
            i += 1
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
