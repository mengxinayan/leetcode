class Solution:
    def reverseVowels(self, s: str) -> str:
        chs = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0
        right = len(chs) - 1
        while left < right:
            if (chs[left] in vowels) and (chs[right] in vowels):
                chs[left], chs[right] = chs[right], chs[left]
                left += 1
                right -= 1
            elif (chs[left] not in vowels) and (chs[right] in vowels):
                left += 1
            elif (chs[left] in vowels) and (chs[right] not in vowels):
                right -= 1
            else:
                left += 1
                right -= 1
        res = ''
        for i in range(len(chs)):
            res += chs[i]
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
