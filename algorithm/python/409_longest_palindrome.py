class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ch_dict = {}
        for i in range(len(s)):
            if s[i] not in ch_dict:
                ch_dict[s[i]] = 1
            else:
                ch_dict[s[i]] += 1
        odd_times = []
        even_times = []
        for value in ch_dict.values():
            if value % 2 == 1:
                odd_times.append(value)
            else:
                even_times.append(value)
        if len(odd_times) == 0: # No odd times char in string
            return sum(even_times)
        else:
            return sum(even_times) + sum(odd_times) - len(odd_times) + 1

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
