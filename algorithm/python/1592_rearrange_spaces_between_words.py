class Solution:
    def reorderSpaces(self, text: str) -> str:
        word_list = []
        num_of_spaces = 0
        tmp = ''    
        for ch in text:
            if ch == ' ':
                num_of_spaces += 1
                if tmp != '':
                    word_list.append(tmp)
                    tmp = ''
            else:
                tmp += ch
        if tmp != '':
            word_list.append(tmp)
            tmp = ''
        if num_of_spaces == 0:
            return text
        if len(word_list) == 1:
            return word_list[0] + num_of_spaces * ' '
        avg = num_of_spaces // (len(word_list) - 1)
        remain = num_of_spaces % (len(word_list) - 1)
        ans = ''
        for i in range(len(word_list)):
            if i < len(word_list) - 1:
                ans = ans + word_list[i] + ' ' * avg
            else:
                ans = ans + word_list[i] + ' ' * remain
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
