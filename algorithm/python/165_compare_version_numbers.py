class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        def compare_version(v1: List[str], v2: List[str]) -> int:
            if len(v1) < len(v2):
                v1 += ['0'] * (len(v2) - len(v1))
            elif len(v1) > len(v2):
                v2 += ['0'] * (len(v1) - len(v2))
            else:
                pass
            ans = 0
            for i in range(len(v1)):
                if int(v1[i]) < int(v2[i]):
                    ans = -1
                    break
                elif int(v1[i]) > int(v2[i]):
                    ans = 1
                    break
                else:
                    pass
            return ans
        
        v1 = version1.split('.')
        v2 = version2.split('.')
        return compare_version(v1, v2)

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
