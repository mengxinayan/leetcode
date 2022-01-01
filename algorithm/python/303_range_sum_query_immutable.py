# Solution 1

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums[:]

    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        for index in range(i, j+1):
            ans += self.arr[index]
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# Solution 2

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_sum = []
        for i in range(len(nums)):
            if i == 0:
                self.nums_sum.append(nums[i])
            else:
                self.nums_sum.append(self.nums_sum[i-1]+nums[i])

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.nums_sum[j]
        else:
            return self.nums_sum[j] - self.nums_sum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

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
