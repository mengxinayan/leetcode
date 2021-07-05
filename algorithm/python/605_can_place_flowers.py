class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) <= 2:
            if (sum(flowerbed) + n) <= 1:
                return True
            else:
                return False
        else:
            count = i = 0
            while i < len(flowerbed):
                if flowerbed[i] == 0:
                    if i == 0:
                        if flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            count += 1
                    elif i == len(flowerbed)-1:
                        if (flowerbed[i-1] == 0):
                            flowerbed[i] = 1
                            count += 1
                    else:
                        if (flowerbed[i-1] == 0) and (flowerbed[i+1] == 0):
                            flowerbed[i] = 1
                            count += 1
                i += 1
            if count >= n:
                return True
            else:
                return False

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
