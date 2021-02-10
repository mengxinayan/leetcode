class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtracking(tmp: str, left: int, right: int):
            if (left == n) and (right == n):
                res.append(tmp)
            if left < n:
                tmp += '('
                backtracking(tmp, left+1, right)
                tmp = tmp[:len(tmp)-1]
            if right < left:
                tmp += ')'
                backtracking(tmp, left, right+1)
                tmp = tmp[:len(tmp)-1]
        
        res = []
        backtracking('', 0, 0)
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
