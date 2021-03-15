class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_index_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_index_dict:
                num_index_dict[nums[i]] = [i]
            else:
                num_index_dict[nums[i]].append(i)
        max_degree_nums = []
        max_degree = -1
        for num in num_index_dict.keys():
            if max_degree < len(num_index_dict[num]):
                max_degree = len(num_index_dict[num])
                max_degree_nums = [num]
            elif max_degree == len(num_index_dict[num]):
                max_degree_nums.append(num)
            else:
                pass
        ans = len(nums)+1
        for number in max_degree_nums:
            ans = min(ans, num_index_dict[number][-1]-num_index_dict[number][0]+1)
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
