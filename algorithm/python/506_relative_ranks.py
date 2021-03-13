class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        ans = ['' for i in range(len(nums))]
        num_index = {}
        for i in range(len(nums)):
            num_index[nums[i]] = i
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if i == 0:
                ans[num_index[nums[i]]] = 'Gold Medal'
            elif i == 1:
                ans[num_index[nums[i]]] = 'Silver Medal'
            elif i == 2:
                ans[num_index[nums[i]]] = 'Bronze Medal'
            else:
                ans[num_index[nums[i]]] = str(i+1)
        return ans

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
