class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        index_zero = 0
        if 0 in A:
            index_zero = A.index(0)
        else:
            index_zero = -1
        if index_zero == -1:
            below_zero = -1
            for i in range(len(A)):
                if A[i] > 0:
                    below_zero = i
                    break
            if below_zero >= K:
                i = 0
                while i < K:
                    A[i] = -A[i]
                    i += 1
            else:
                i = 0
                while i < K:
                    if i < below_zero:
                        A[i] = -A[i]
                    else:
                        if below_zero != 0:
                            if abs(A[below_zero-1]) <= abs(A[below_zero]):
                                A[below_zero-1] = -A[below_zero-1]
                            else:
                                A[below_zero] = -A[below_zero]
                        else:
                            A[0] = -A[0]
                    i += 1
        else:
            i = 0
            while i < min(K, index_zero):
                A[i] = -A[i]
                i += 1
        return sum(A)

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
