class Solution:
    def findMin(self, nums: List[int]) -> int:

        def binary_search(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            if nums[left] < nums[right]:
                return nums[left]
            else:
                mid = left + (right - left) // 2
                if left == mid:
                    return min(nums[left], binary_search(mid+1, right))
                if right == mid:
                    return min(nums[right], binary_search(left, mid))
                if nums[left] < nums[mid]:
                    return binary_search(mid+1, right)
                else:
                    return binary_search(left, mid)

        if len(nums) == 1:
            return nums[0]
        min_number = binary_search(0, len(nums)-1)
        return min_number

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
