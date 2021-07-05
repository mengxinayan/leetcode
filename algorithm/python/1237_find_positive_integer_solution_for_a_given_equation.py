"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

# Solution 1, Brute-force

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        curr_max_y = 1001
        for i in range(1, 1001):
            left = 1
            right = curr_max_y
            while left <= right:
                mid = (left + right) // 2
                if customfunction.f(i, mid) > z:
                    right = mid - 1
                elif customfunction.f(i, mid) < z:
                    left = mid + 1
                else:
                    ans.append([i, mid])
                    curr_max_y = mid
                    break
        return ans


# Solution 2, Binary Search

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for i in range(1, 1001):
            left = 1
            right = 1001
            while left <= right:
                mid = (left + right) // 2
                if customfunction.f(i, mid) > z:
                    right = mid - 1
                elif customfunction.f(i, mid) < z:
                    left = mid + 1
                else:
                    ans.append([i, mid])
                    break
        return ans


# Solution 3, Two Pointers

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        curr_x = 1
        curr_y = 1000
        while (curr_x <= 1000) and (curr_y >= 1):
            tmp = customfunction.f(curr_x, curr_y)
            if tmp < z:
                curr_x += 1
            elif tmp > z:
                curr_y -= 1
            else:
                ans.append([curr_x, curr_y])
                curr_x += 1
                curr_y -= 1
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
