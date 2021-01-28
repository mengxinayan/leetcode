class Solution:
    def maximumTime(self, time: str) -> str:
        res = ''
        if time[0] == '?':
            # ?4:03
            if (time[1].isdigit() == True) and (int(time[1]) >= 4):
                res += '1'
            else:
                res += '2'
        else:
            res += time[0]
        if time[1] == '?':
            # ??:3?
            if (time[0] == '2') or (time[0] == '?'):
                res += '3'
            else:
                res += '9'
        else:
            res += time[1]
        res += time[2]
        if time[3] == '?':
            res += '5'
        else:
            res += time[3]
        if time[4] == '?':
            res += '9'
        else:
            res += time[4]
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
