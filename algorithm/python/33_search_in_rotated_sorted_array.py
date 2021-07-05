class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search_in_sorted(left: int, right: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            else:
                return -1

        def binary_search_in_unsorted(left: int, right: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                if nums[left] <= nums[mid]:
                    if nums[left] <= target < nums[mid]:
                        return binary_search_in_sorted(left, mid-1)
                    else:
                        return binary_search_in_unsorted(mid+1, right)
                else:
                    if nums[mid] < target <= nums[right]:
                        return binary_search_in_sorted(mid+1, right)
                    else:
                        return binary_search_in_unsorted(left, mid-1)
            else:
                return -1

        ans = binary_search_in_unsorted(0, len(nums)-1)
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
