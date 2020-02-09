class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_times = {}
        for i in range(len(nums)):
            if nums[i] in num_times:
                num_times[nums[i]] += 1
            else:
                num_times[nums[i]] = 1
        res = times = 0
        for key, value in num_times.items():
            if times < value:
                res = key
                times = value
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
    MERCHANTABILITY or FITNESS FOR A pRTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''