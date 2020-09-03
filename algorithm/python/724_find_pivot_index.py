class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        left_sum = [nums[0]]
        right_sum = [nums[-1]]
        for i in range(1, len(nums)):
            left_sum.append(left_sum[i-1]+nums[i])
            right_sum.append(right_sum[i-1]+nums[-i-1])
        right_sum.reverse()
        res = -1
        for i in range(len(left_sum)):
            if left_sum[i] == right_sum[i]:
                res = i
                break
        return res

'''
    This is my personal record of solving Leetcode Problems. 
    If you have any questions, please discuss them in [Issues](https://github.com/mengxinayan/leetcode/issues).
    Copyright (C) 2020  mengxinayan

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
