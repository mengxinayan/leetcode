class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def is_complete_circuit(index: int) -> bool:
            ans = True
            i = 0
            now = 0
            while i < length:
                now = now + gas[index%length] - cost[index%length]
                if now < 0:
                    ans = False
                    break
                else:
                    index += 1
                    i += 1
            return ans

        length = len(gas)
        ans = -1
        for i in range(length):
            if is_complete_circuit(i) == True:
                ans = i
                break
        return ans

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
