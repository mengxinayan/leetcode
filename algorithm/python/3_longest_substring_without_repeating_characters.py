class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        max_num = curr_num = 0
        ch_set = {}
        i = 0
        while i < len(s):
            if s[i] not in ch_set:
                ch_set[s[i]] = i
                curr_num += 1
            else:
                max_num = max(max_num, curr_num)
                i = ch_set[s[i]] + 1
                ch_set.clear()
                ch_set[s[i]] = i
                curr_num = 1
            i += 1
        max_num = max(max_num, curr_num)
        return max_num

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
