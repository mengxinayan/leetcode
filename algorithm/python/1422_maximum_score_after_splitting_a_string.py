# Solution 1

class Solution:
    def maxScore(self, s: str) -> int:
        max_score = -1
        for i in range(1, len(s)):
            max_score = max(max_score, s[:i].count('0') + s[i:].count('1'))
        return max_score


# Solution 2

class Solution:
    def maxScore(self, s: str) -> int:
        count = 0
        zero_score = []
        for ch in s:
            if ch == '0':
                count += 1
            zero_score.append(count)
        count = 0
        one_score = []
        for ch in s[::-1]:
            if ch == '1':
                count += 1
            one_score.insert(0, count)
        max_score = -1
        for i in range(1, len(zero_score)):
            max_score = max(max_score, zero_score[i-1]+one_score[i])
        return max_score

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
