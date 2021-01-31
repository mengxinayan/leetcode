# Solution 1: Dynamic Programming(may be exceed time limit)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        length = len(s)
        dp = [[False] * length for i in range(length)]
        for l in range(length):
            for i in range(length):
                j = i + l
                if j > length - 1:
                    break
                if l == 0:
                    dp[i][i] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if (dp[i][j] == True) and (l+1 > len(res)):
                    res = s[i:j+1]
        return res


# Solution 2: Expand from center string

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_substr(left: int, right: int) -> int:
            while (left >= 0) and (right <= len(s) - 1) and (s[left] == s[right]):
                left -= 1
                right += 1
            return left+1, right-1

        start = end = -1
        for i in range(len(s)):
            left1, right1 = expand_substr(i, i)
            left2, right2 = expand_substr(i, i+1)
            if (end - start) < (right1 - left1 + 1):
                start, end = left1, right1+1
            if (end - start) < (right2 - left2 + 1):
                start, end = left2, right2+1
        return s[start:end]

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
