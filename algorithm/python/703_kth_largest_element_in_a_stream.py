# Solution 1

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums[:]
        self.arr.sort(reverse=True)
        if len(self.arr) > k:
            self.arr = self.arr[:k]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            self.arr.append(val)
        elif (len(self.arr) == self.k) and (val > self.arr[-1]):
            self.arr.pop()
            self.arr.append(val)
        else:
            pass
        self.arr.sort(reverse=True)
        return self.arr[-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# Solution 2

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif (len(self.heap) == self.k) and (val > self.heap[0]):
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

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
