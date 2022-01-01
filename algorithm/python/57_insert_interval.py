class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        for i in range(len(intervals)-1):
            if intervals[i][0] == newInterval[0]:
                if intervals[i][1] < newInterval[1]:
                    intervals.insert(i+1, newInterval)
                else:
                    intervals.insert(i, newInterval)
                break
            elif intervals[i][0] < newInterval[0] < intervals[i+1][0]:
                intervals.insert(i+1, newInterval)
                break
            elif (i == 0) and (intervals[i][0] > newInterval[0]):
                intervals.insert(i, newInterval)
            else:
                pass
        else:
            intervals.append(newInterval)
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        else:
            ans.append([start, end])
        return ans

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
