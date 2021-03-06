class Solution:
    def isValid(self, s: str) -> bool:
        # 只输入一个右括号"]"
        if len(s) == 0:
            return True
        chs = []
        ans = False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                chs.append(s[i])
            elif s[i] == ')':
                if len(chs) == 0 or chs[-1] != '(':
                    chs.append(' ')
                    break
                else:
                    chs.pop()
            elif s[i] == ']':
                if len(chs) == 0 or chs[-1] != '[':
                    chs.append(' ')
                    break
                else:
                    chs.pop()
            elif s[i] == '}':
                if len(chs) == 0 or chs[-1] != '{':
                    chs.append(' ')
                    break
                else:
                    chs.pop()
            else:
                pass
        if len(chs) == 0:
            ans = True
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
