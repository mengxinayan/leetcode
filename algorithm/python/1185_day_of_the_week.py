class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        def is_leap_year(year: int) -> bool:
            if (year % 4 == 0) and (year % 100 != 0):
                return True
            elif (year % 400 == 0):
                return True
            else:
                return False

        def cal_month_day(year: int) -> List[int]:
            if is_leap_year(year) == True:
                return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def cal_num_of_day(day: int, month: int, year: int) -> int:
            res = 0
            for i in range(1971, year):
                if is_leap_year(i) == True:
                    res += 366
                else:
                    res += 365
            month_day = cal_month_day(year)
            res += sum(month_day[:month-1]) + day
            return res
        
        ans_values = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        num_of_day = cal_num_of_day(day, month, year)
        return ans_values[(num_of_day+3)%7]

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
