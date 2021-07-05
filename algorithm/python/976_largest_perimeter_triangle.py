class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        '''
        1. 假设有 a, b, c 三边，三边的长度关系为：a <= b <= c，判断其是否为三角形的条件只需判断： a < b + c 成立即可
        理由：如果 a < b + c 成立，那么 b < a + c，c < a + b 必然成立。而 a < b + c 通过变化很容易证明 c > a - b 成立
        2. 排序后的从大到小相邻的三边一定是周长最大的解（前提是能构成三角形）。
        假设存在 x0 <= x1 <= x2 <= x3 <= x4 若干边，如果 x2 + x3 <= x4 的不成立话，那么 x1 + x3 <= x4 也无法成立，因此要想周长最大且能构成三角形，得是排序后相邻的三条边。
        
        1. Assuming there are three sides a, b, c, the length relationship of the three sides is: a <= b <= c, the condition for judging whether it is a triangle only needs to judge: a <b + c.
        Reason: If a <b + c holds, then b <a + c, c <a + b must hold. And a <b + c can easily prove that c> a-b is true by changing
        2. After sorting, the three adjacent sides from largest to smallest must be the solution with the largest perimeter (provided that it can form a triangle).
        Suppose there are several sides x0 <= x1 <= x2 <= x3 <= x4, if x2 + x3 <= x4 does not hold, then x1 + x3 <= x4 also cannot hold, so you want to have the largest circumference and form a triangle , Must be the three adjacent edges after sorting.
        '''
        A.sort()
        for i in range(len(A)-1, 1, -1):
            a = A[i]
            b = A[i-1]
            c = A[i-2]
            if a < b + c:
                return a + b + c
        else:
            return 0

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
