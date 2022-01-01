# Solution 1. Traverse search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return False
        ans = 0
        for i in range(1, len(arr)-1):
            if (arr[i-1] < arr[i]) and (arr[i] > arr[i+1]):
                ans = i
                break
        return ans


# Solution 2. Binary search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return False
        left = 0
        right = len(arr)-1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid + 1
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                right = mid - 1
            else:
                ans = mid
                break
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
