class Solution:
    def reformatNumber(self, number: str) -> str:
        num_list = []
        for ch in number:
            if ch.isdigit() == True:
                num_list.append(ch)
                
        length = len(num_list)
        start = 0
        insert_position = []
        if length % 3 == 0:
            start = -3
        elif length % 3 == 1:
            start = -4
            insert_position = [-2]
        else:
            start = -2
        for i in range(start, -len(num_list), -3):
            insert_position.append(i)
        insert_position_set = set(insert_position)
        ans = ''
        for i in range(-1, -len(num_list)-1, -1):
            ans = num_list[i] + ans
            if i in insert_position_set:
                ans = '-' + ans
        return ans

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020-2022  mengxinayan

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
