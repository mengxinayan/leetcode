class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] = A[-1] + K
        for i in range(len(A)-1, 0, -1):
            if A[i] >= 10:
                tmp = A[i]
                A[i] = tmp % 10
                A[i-1] = A[i-1] + tmp // 10
        while A[0] >= 10:
            tmp = A[0]
            A[0] = tmp % 10
            A.insert(0, tmp//10)
        return A

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
