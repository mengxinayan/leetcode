# Solution 1

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ch_dict = {}
        for i in range(len(t)):
            if t[i] not in ch_dict:
                ch_dict[t[i]] = 1
            else:
                ch_dict[t[i]] += 1
        ans = ''
        for i in range(len(s)):
            if s[i] in ch_dict:
                if ch_dict[s[i]] == 1:
                    del ch_dict[s[i]]
                else:
                    ch_dict[s[i]] -= 1
            else:
                ans = s[i]
                break
        else:
            ans = list(ch_dict.keys())[0]
        return ans


# Solution 2

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = sum2 = 0
        for i in range(len(s)):
            sum1 += ord(s[i])
        for i in range(len(t)):
            sum2 += ord(t[i])
        return chr(sum2 - sum1)

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
