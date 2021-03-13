class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        def cal_point_distance(a: List[int], b: List[int]) -> int:
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        def cal_point_num_of_boomerangs(point: List[int], others: List[List[int]]) -> int:
            path_len_dict = {}
            for i in range(len(others)):
                tmp = cal_point_distance(point, others[i])
                if tmp not in path_len_dict:
                    path_len_dict[tmp] = 1
                else:
                    path_len_dict[tmp] += 1
            ans = 0
            for value in path_len_dict.values():
                if value > 1:
                    ans += value * (value-1)
            return ans
        
        ans = 0
        for i in range(len(points)):
            ans += cal_point_num_of_boomerangs(points[i], points[:i] + points[i+1:])
        return ans

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
