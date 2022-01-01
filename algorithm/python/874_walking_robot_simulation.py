class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = 0 # 0 = north, 1 = east, 2 = south, 3 = west
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obstacles_set = set(map(tuple, obstacles))
        x = y = ans = 0
        for cmd in commands:
            if cmd == -1: # turn right
                direction = (direction + 1) % 4
            elif cmd == -2: # turn left
                direction = (direction - 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[direction], y+dy[direction]) not in obstacles_set:
                        x += dx[direction]
                        y += dy[direction]
                        ans = max(ans, x*x+y*y)
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
