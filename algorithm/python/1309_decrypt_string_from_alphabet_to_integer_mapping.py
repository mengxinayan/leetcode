class Solution:
    def freqAlphabets(self, s: str) -> str:
        char_str = '-abcdefghijklmnopqrstuvwxyz'
        i = 0
        res = ''
        index = -1
        while i != len(s):
            if (i+2 < len(s)) and (s[i+2] == '#'):
                index = int(s[i:i+2])
                res += char_str[index]
                i += 3
            else:
                index = int(s[i])
                res += char_str[index]
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
