class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes.insert(0, 0)
        ch_time_dict = {}
        for i in range(len(keysPressed)):
            if keysPressed[i] not in ch_time_dict:
                ch_time_dict[keysPressed[i]] = releaseTimes[i+1] - releaseTimes[i]
            else:
                ch_time_dict[keysPressed[i]] = max(ch_time_dict[keysPressed[i]], releaseTimes[i+1]-releaseTimes[i])
        max_time = -1
        max_ch = ''
        for key in ch_time_dict.keys():
            if ch_time_dict[key] > max_time:
                max_ch = key
                max_time = ch_time_dict[key]
            elif ch_time_dict[key] == max_time:
                max_ch += key
            else:
                pass
        return max(max_ch)

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
