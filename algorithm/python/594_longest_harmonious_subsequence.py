class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_times = {}
        for i in range(len(nums)):
            if nums[i] not in num_times:
                num_times[nums[i]] = 1
            else:
                num_times[nums[i]] += 1
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            max_length = max(max_length, \
                            (num_times[num-1] + num_times[num]) if (num-1 in num_times) else 0, \
                            (num_times[num+1] + num_times[num]) if (num+1 in num_times) else 0)
        return max_length

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
