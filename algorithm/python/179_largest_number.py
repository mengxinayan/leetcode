class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def my_cmp(num1: str, num2: str) -> int:
            if num1 == num2:
                return 0
            tmp1 = num1 + num2
            tmp2 = num2 + num1
            if tmp1 > tmp2:
                return 1
            else:
                return -1

        if len(nums) == 1:
            return str(nums[0])
        else:
            # Special case: [0, 0] -> '0'
            if sum(nums) == 0:
                return '0'
            str_nums = []
            for num in nums:
                str_nums.append(str(num))
            str_nums.sort(key=cmp_to_key(my_cmp), reverse=True)
            ans = ''
            for i in range(len(str_nums)):
                ans += str(str_nums[i])
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
