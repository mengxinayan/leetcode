class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = -1
        max_num = second_max_num = -1
        for i in range(len(nums)):
            if nums[i] > max_num:
                second_max_num = max_num
                max_num = nums[i]
                max_index = i
            elif (max_num >= nums[i]) and (nums[i] > second_max_num):
                second_max_num = nums[i]
            else:
                pass
        if max_num >= 2*second_max_num:
            return max_index
        else:
            return -1

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
