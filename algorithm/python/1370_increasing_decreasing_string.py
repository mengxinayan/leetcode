class Solution:
    def sortString(self, s: str) -> str:
        ch_dict = {}
        for ch in s:
            if ch not in ch_dict:
                ch_dict[ch] = 1
            else:
                ch_dict[ch] += 1
        ch_arr = list(ch_dict.keys())
        ch_arr.sort()
        ch_arr_reversed = ch_arr[::-1]
        ans = ''
        while len(ch_dict) != 0:
            for ch in ch_arr:
                if ch in ch_dict:
                    ans += ch
                    ch_dict[ch] -= 1
                    if ch_dict[ch] == 0:
                        del ch_dict[ch]
            for ch in ch_arr_reversed:
                if ch in ch_dict:
                    ans += ch
                    ch_dict[ch] -= 1
                    if ch_dict[ch] == 0:
                        del ch_dict[ch]
        return ans

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
