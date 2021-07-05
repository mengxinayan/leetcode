class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List_dic = {}
        for i in range(0, len(nums)):
            List_dic[nums[i]] = i
        for i in range(0, len(nums)):
            ans = List_dic.get(target-nums[i], -1)
            if ans != -1 and ans != i:
                return [i, ans]

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
