# Solution 1: Binary Search

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif (n > 0) and (n % 2 == 0):
            return self.myPow(x*x, n/2)
        elif (n > 0) and (n % 2 == 1):
            return self.myPow(x, n-1) * x
        else:
            return 1 / self.myPow(x, -n)


# Solution 2: pow function

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)


# Solution 3: pow operator

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

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
