class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(s: str) -> bool:
            left = 0
            right = len(s)-1
            ans = True
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    ans = False
                    break
            return ans

        if len(s) <= 2:
            return True
        left = 0
        right = len(s)-1
        ans = True
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if (s[left+1] != s[right]) and (s[left] != s[right-1]):
                    ans = False
                else:
                    ans = ( is_palindrome(s[left+1:right+1]) ) or ( is_palindrome(s[left:right]) )
                break
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
