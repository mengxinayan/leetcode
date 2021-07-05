class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length1 = len(haystack)
        length2 = len(needle)
        if length1 > length2:
            ans = -1
            for i in range(0, length1-length2+1):
                # Why '+1'? -> "aab" "ab"
                if haystack[i:i+length2] == needle:
                    ans = i
                    break
            return ans
        elif length1 == length2:
            if haystack == needle:
                return 0
            else:
                return -1
        else:
            return -1

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
