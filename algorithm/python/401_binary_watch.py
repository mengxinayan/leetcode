class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:      

        # def cal_two_num_sum(num: int) -> List[List[int]]

        def combine_hour_and_minute(hour: List[str], minute: List[str]) -> List[str]:
            res = []
            for i in range(len(hour)):
                for j in range(len(minute)):
                    res.append(hour[i] + ':' + minute[j])
            return res
            
        def cal_hour_value(n):
            arr = [1, 2, 4, 8]
            tmp = combination(arr, n)
            res = []
            for nums in tmp:
                t = sum(nums)
                if t < 12:
                    res.append(str(t))
                else:
                    pass
            return res

        def cal_minute_value(n):
            arr = [1, 2, 4, 8, 16, 32]
            tmp = combination(arr, n)
            res = []
            for nums in tmp:
                t = sum(nums)
                if t == 0:
                    res.append('00')
                elif 1 <= t <= 9:
                    res.append('0'+str(t))
                elif 10 <= t < 60:
                    res.append(str(t))
                else:
                    pass
            return res

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
                res = []
                for i in range(num+1):
                    hour = cal_hour_value(i)
                    minute = cal_minute_value(num-i)
                    res.extend(combine_hour_and_minute(hour, minute))
                return res
            else:
                res = []
                for i in range(5):
                    hour = cal_hour_value(i)
                    minute = cal_minute_value(num-i)
                    res.extend(combine_hour_and_minute(hour, minute))
                return res

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
