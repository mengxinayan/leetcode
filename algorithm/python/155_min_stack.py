class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.min_val = float('inf')

    def push(self, x: int) -> None:
        self.nums.append(x)
        if x < self.min_val:
            self.min_val = x

    def pop(self) -> None:
        self.nums.pop()
        if len(self.nums) == 0: # Don't Forget this case !!!
            self.min_val = float('inf')
        else:
            self.min_val = min(self.nums)

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

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
