class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def cal_next(nums: List[int]) -> List[int]:
            res = [0 for i in range( len(nums)+1 )]
            res[0] = 1
            res[-1] = 1
            for i in range(1, len(nums)):
                res[i] = nums[i] + nums[i-1]
            return res

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            res = [1,1]
            for i in range(rowIndex-1):
                res = cal_next(res)
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