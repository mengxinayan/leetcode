class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:

        def cal_odd_even_str(string: str) -> str:
            odd = []
            even = []
            for i in range(0, len(string), 2):
                even.append(string[i])
            for i in range(1, len(string), 2):
                odd.append(string[i])
            odd.sort()
            even.sort()
            return str(odd) + str(even)
        
        odd_even_set = set()
        for string in A:
            odd_even_set.add(cal_odd_even_str(string))
        return len(odd_even_set)

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
