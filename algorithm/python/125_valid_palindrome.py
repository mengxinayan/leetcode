class Solution:
    def isPalindrome(self, s: str) -> bool:

        def process(s: str) -> str:
            ans = ''
            for i in range(len(s)):
                if s[i].isalnum():
                    ans += s[i]
            return ans.lower()
        
        if len(s) == 0 or len(s) == 1:
            return True
        processed_str = process(s)
        ans = False
        left = 0
        right = len(processed_str) - 1
        while left < right:
            if processed_str[left] != processed_str[right]:
                break
            left += 1
            right -= 1
        else:
            ans = True
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
