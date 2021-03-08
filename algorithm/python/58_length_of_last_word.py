class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '': # 第一次漏掉了这种情况
            return 0
        ans = 0
        index = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                index = i
                break
        for i in range(index, -1, -1):
            if s[i] != ' ':
                ans += 1
            else:
                break
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
