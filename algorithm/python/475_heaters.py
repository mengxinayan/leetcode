class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def cal_nearest_heater_distance(house: int) -> int:
            ans = 0
            left = 0
            right = len(heaters) - 1
            mid = (left + right) // 2
            while left < right:
                if heaters[mid] < house:
                    left = mid + 1
                    mid = (left + right) // 2
                elif heaters[mid] > house:
                    right = mid
                    mid = (left + right) // 2
                else:
                    break
            else:
                if left >= len(heaters) - 1:
                    ans = min(abs(heaters[left-1]-house), abs(heaters[left]-house))
                elif right <= 0:
                    ans = min(abs(heaters[0]-house), abs(heaters[1]-house))
                else:
                    ans = min(abs(heaters[mid-1]-house), abs(heaters[mid]-house),abs(heaters[mid+1]-house))
            return ans
        
        heaters.sort()
        ans_arr = []
        for i in range(len(houses)):
            ans_arr.append(cal_nearest_heater_distance(houses[i]))
        return max(ans_arr)

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
