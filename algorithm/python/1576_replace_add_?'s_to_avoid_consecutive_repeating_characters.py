class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) == 1:
            if s == '?':
                return 'a'
            else:
                return s
        ch_list = list(s)
        for i in range(len(ch_list)):
            if ch_list[i] == '?':
                if i == 0:
                    if ch_list[1] != 'a':
                        ch_list[0] = 'a'
                    else:
                        ch_list[0] = 'b'
                elif i == len(ch_list)-1:
                    if ch_list[len(ch_list)-2] != 'a':
                        ch_list[len(ch_list)-1] = 'a'
                    else:
                        ch_list[len(ch_list)-1] = 'b'
                else:
                    if (ch_list[i-1] != 'a') and (ch_list[i+1] != 'a'):
                        ch_list[i] = 'a'
                    elif (ch_list[i-1] != 'b') and (ch_list[i+1] != 'b'):
                        ch_list[i] = 'b'
                    else:
                        ch_list[i] = 'c'
        ans = ''
        for ch in ch_list:
            ans += ch
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
