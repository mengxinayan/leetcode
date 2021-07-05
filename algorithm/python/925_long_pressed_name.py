class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        if (len(name) == len(typed)) and (name == typed):
            return True
        name_i = 0
        typed_i = 0
        ans = True
        while (name_i != len(name)) and (typed_i != len(typed)):
            if name[name_i] != typed[typed_i]:
                if (typed_i != 0) and (typed[typed_i] == typed[typed_i-1]):
                    typed_i += 1
                else:
                    ans = False
                    break
            else:
                name_i += 1
                typed_i += 1
        if (name_i == len(name)) and (typed_i <= len(typed)):
            while typed_i != len(typed):
                if typed[typed_i-1] != typed[typed_i]:
                    ans = False
                    break
                typed_i += 1
        elif (name_i < len(name)) and (typed_i == len(typed)):
            ans = False
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
