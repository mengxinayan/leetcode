class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # 使用鞋带公式
        # use Shoelace formula method
        ans=0
        for i in points:
            for j in points:
                for k in points:
                    ans=max(ans,abs(i[0]*j[1]+j[0]*k[1]+k[0]*i[1]-i[1]*j[0]-j[1]*k[0]-k[1]*i[0]))
        return ans/2

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
