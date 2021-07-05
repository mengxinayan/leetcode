class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_arr = str.split()
        if len(pattern) != len(str_arr):
            return False
        str_dict = {}
        for i in range(len(pattern)):
            if pattern[i] not in str_dict:
                if str_arr[i] not in str_dict.values():
                    str_dict[pattern[i]] = str_arr[i]
                else:
                    return False
            else:
                if str_dict[pattern[i]] != str_arr[i]:
                    return False
        else:
            return True

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
