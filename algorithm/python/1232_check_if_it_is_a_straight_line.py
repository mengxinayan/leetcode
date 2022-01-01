class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Because there are no duplicate points, just need to check whether there are points with the same abscissa value.
        # If there is one and only one abscissa value, it indicates that it is a vertical line parallel to the y axis. otherwise it is not a straight line.
        # 因为没有重复的点，所以只需要检查是否存在相同横坐标值的点即可。
        # 若有且只有一个横坐标值，则表明其是一条平行于y轴的竖线，反之不是一条直线
        x_points = []
        for i in range(len(coordinates)):
            x_points.append(coordinates[i][0])
        num_x_points = len(set(x_points))
        if len(x_points) != num_x_points:
            return num_x_points == 1
        a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        b = coordinates[0][1] - a * coordinates[0][0]
        ans = True
        for i in range(2, len(coordinates)):
            if coordinates[i][1] != a * coordinates[i][0] + b:
                ans = False
                break
        return ans

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
