class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(string: str) -> bool:
            left = 0
            right = len(string) - 1
            ans = True
            while left <= right:
                if string[left] != string[right]:
                    ans = False
                    break
                else:
                    left += 1
                    right -= 1
            return ans

        def sum_length(arr: List[str]):
            ans = 0
            for tmp in arr:
                ans += len(tmp)
            return ans

        def partition_string(string: str, tmp: List[str]):
            if sum_length(tmp) == len(s):
                ans.append(tmp)
                return 
            for i in range(len(string)):
                if is_palindrome(string[:i+1]) == True:
                    partition_string(string[i+1:], tmp+[string[:i+1]])
                else:
                    continue

        if len(s) == 0:
            return [[]]
        elif len(s) == 1:
            return [[s]]
        else:
            ans = []
            partition_string(s, [])
            return ans

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
