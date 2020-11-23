class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-weight for weight in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            max_weight = heapq.heappop(stones_heap)
            second_weight = heapq.heappop(stones_heap)
            if max_weight != second_weight:
                heapq.heappush(stones_heap, max_weight-second_weight)
        if len(stones_heap) == 1:
            return -stones_heap[0]
        else:
            return 0

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
