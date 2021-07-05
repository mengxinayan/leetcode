class Solution:
    def maximumTime(self, time: str) -> str:
        ans = ''
        if time[0] == '?':
            # ?4:03
            if (time[1].isdigit() == True) and (int(time[1]) >= 4):
                ans += '1'
            else:
                ans += '2'
        else:
            ans += time[0]
        if time[1] == '?':
            # ??:3?
            if (time[0] == '2') or (time[0] == '?'):
                ans += '3'
            else:
                ans += '9'
        else:
            ans += time[1]
        ans += time[2]
        if time[3] == '?':
            ans += '5'
        else:
            ans += time[3]
        if time[4] == '?':
            ans += '9'
        else:
            ans += time[4]
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
