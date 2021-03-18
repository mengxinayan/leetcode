class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_A = sum(A)
        if sum_A % 3 != 0:
            return False
        equal_sum = sum_A // 3
        single_sum = 0
        left = 1
        left_ans = False
        left_sum = A[0]
        while (left != len(A)) and (left_sum != equal_sum):
            left_sum += A[left]
            left += 1
        if left < len(A):
            left_ans = True
            left -= 1
        right = len(A) - 1 - 1
        right_ans = False
        right_sum = A[-1]
        while (right != -1) and (right_sum != equal_sum):
            right_sum += A[right]
            right -= 1
        if right > -1:
            right_ans = True
            right += 1
        return left_ans and right_ans and (right - left > 1)

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
