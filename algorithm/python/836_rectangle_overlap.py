class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if (rec2[0] >= rec1[2]) or (rec2[2] <= rec1[0]) or (rec2[1] >= rec1[3]) or (rec2[3] <= rec1[1]):
            return False
        return True

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
    alon
