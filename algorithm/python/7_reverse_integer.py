class Solution:
    def reverse(self, x: int) -> int:
        '''
        32 bit signed integer
        2^31-1 = 2147483647
        -2^31 = -2147483648
        '''
        if x == 0:
            return 0
        falg = 1
        nums = list(str(x))
        if nums[0] == '-':
            falg = -1
            nums = nums[1:]
        nums.reverse()
        while(nums[0] == '0'):
            nums = nums[1:]
        res = int(nums[0])
        for i in range(1, len(nums)):
            res = res * 10 + int(nums[i])
        res = res * falg
        if res > 2147483647 or res < -2147483648:
            return 0
        else:
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
