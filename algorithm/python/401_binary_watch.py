class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        def combine_hour_and_minute(hour: List[str], minute: List[str]) -> List[str]:
            ans = []
            for i in range(len(hour)):
                for j in range(len(minute)):
                    ans.append(hour[i] + ':' + minute[j])
            return ans

        def cal_hour_value(n):
            arr = [1, 2, 4, 8]
            tmp = combination(arr, n)
            ans = []
            for nums in tmp:
                t = sum(nums)
                if t < 12:
                    ans.append(str(t))
                else:
                    pass
            return ans

        def cal_minute_value(n):
            arr = [1, 2, 4, 8, 16, 32]
            tmp = combination(arr, n)
            ans = []
            for nums in tmp:
                t = sum(nums)
                if t == 0:
                    ans.append('00')
                elif 1 <= t <= 9:
                    ans.append('0'+str(t))
                elif 10 <= t < 60:
                    ans.append(str(t))
                else:
                    pass
            return ans

        def combination(L, k): # C(n,k) = C(n-1,k) + C(n-1,k-1)
            if k >= len(L):
                return [L]
            if k == 0:
                return [[]]
            T1 = combination(L[0:len(L)-1], k-1)
            T2 = combination(L[0:len(L)-1], k)
            T = []
            for e in T1:
                e.append(L[len(L)-1])
                T.append(e)
            return T2 + T

        if num == 0:
                return ['0:00']
        elif num > 10:
                return []
        else:
            if num <= 4:
                ans = []
                for i in range(num+1):
                    hour = cal_hour_value(i)
                    minute = cal_minute_value(num-i)
                    ans.extend(combine_hour_and_minute(hour, minute))
                return ans
            else:
                ans = []
                for i in range(5):
                    hour = cal_hour_value(i)
                    minute = cal_minute_value(num-i)
                    ans.extend(combine_hour_and_minute(hour, minute))
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
