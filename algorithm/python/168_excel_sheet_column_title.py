class Solution:
    def convertToTitle(self, n: int) -> str:
        chars = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',\
                 'O','P','Q','R','S','T','U','V','W','X','Y']
        nums = []
        while n != 0:
            nums.append(n % 26)
            '''
            减一的原因是为了将 26 映射为 'Z' 而不是 'AZ'
            The reason for subtracting one is to map 26 to 'Z' instead of 'AZ'
            '''
            if n % 26 == 0:
                n -= 1
            n = n // 26
        nums.reverse()
        res = ''
        for i in range(len(nums)):
            res += (chars[nums[i]])
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