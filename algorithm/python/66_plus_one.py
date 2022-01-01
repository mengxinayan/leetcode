class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            if digits[0] == 9:
                return [1, 0]
            else:
                return [digits[0]+1]
        nums = digits[:] # Promise won't change digits
        nums[len(nums)-1] += 1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == 10:
                nums[i] = 0
                nums[i-1] += 1
            else:
                break
        else:
            if nums[0] == 10: # [10, 0, 0]
                nums[0] = 0
                nums.insert(0, 1)
        return nums

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
