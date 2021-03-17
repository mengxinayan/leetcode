class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        begin = 0
        last = len(S) - 1
        ans = ''
        while begin != len(S):
            if (S[begin].isalpha() == True) and (S[last].isalpha() == True):
                ans += S[last]
                begin += 1
                last -= 1
            elif (S[begin].isalpha() == True) and (S[last].isalpha() == False):
                while S[last].isalpha() == False:
                    last -= 1
                ans += S[last]
                begin += 1
                last -= 1
            elif (S[begin].isalpha() == False) and (S[last].isalpha() == True):
                ans += S[begin]
                begin += 1
            else:
                ans += S[begin]
                begin += 1
                last -= 1
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
