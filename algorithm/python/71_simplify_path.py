class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        dots_set = {'', '.', '..'}
        path_arr = path.split('/')
        for path_str in path_arr:
            if path_str not in dots_set:
                path_stack.append(path_str)
            elif (path_str == '..') and (len(path_stack) != 0):
                path_stack.pop()
        ans = '/' + '/'.join(path_stack)
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
