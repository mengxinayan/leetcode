class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token in operators:
                tmp = 0
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                if token == '+':
                    tmp = tmp2 + tmp1
                elif token == '-':
                    tmp = tmp2 - tmp1
                elif token == '*':
                    tmp = tmp2 * tmp1
                elif token == '/':
                    tmp = int(tmp2 / tmp1)
                stack.append(tmp)
            else:
                stack.append(int(token))
        return stack[0]

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
