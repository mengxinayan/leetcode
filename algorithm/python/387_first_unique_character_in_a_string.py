class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_dict = {}
        ch_set = set([])
        for i in range(len(s)):
            if s[i] not in ch_set:
                ch_set.add(s[i])
                index_dict[s[i]] = i
            else:
                if s[i] in index_dict:
                    del index_dict[s[i]]
        if len(index_dict) == 0:
            return -1
        else:
            return min(index_dict.values())

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
