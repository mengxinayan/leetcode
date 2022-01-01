class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.nums.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = []
        while len(self.nums) != 1:
            tmp.append(self.nums.pop())
        ans = self.nums.pop()
        tmp.reverse()
        for i in range(len(tmp)):
            self.nums.append(tmp[i])
        return ans 
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.nums[0]

        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.nums) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

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
