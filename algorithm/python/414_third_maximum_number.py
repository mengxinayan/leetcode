class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        number_set = set(nums)
        max_three_number = []
        max_number = 0
        for number in number_set:
            if len(max_three_number) < 3:
                max_three_number.append(number)
                if number > max_number:
                    max_number = number
            else:
                if number > max_number:
                    max_number = number
                    max_three_number.remove(min(max_three_number))
                    max_three_number.append(max_number)
        if len(max_three_number) < 3:
            return max_number
        else:
            return min(max_three_number)

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
