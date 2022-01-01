class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        def cal_sum(s1: str, s2: str) -> str: # len(s1) >= len(s2)
            s2 = s2.rjust(len(s1), '0')
            ans = ''
            flag = 0
            for i in range(len(s1)-1, -1, -1):
                tmp = ord(s1[i]) - ord('0') + ord(s2[i]) - ord('0') + flag
                if tmp >= 10:
                    ans = str(tmp-10) + ans
                    flag = 1
                else:
                    ans = str(tmp) + ans
                    flag = 0
            if flag == 1:
                ans = str(flag) + ans
            return ans
        
        if len(num1) >= len(num2):
            return cal_sum(num1, num2)
        else:
            return cal_sum(num2, num1)

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
