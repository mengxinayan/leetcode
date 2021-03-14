class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        def str_to_dict(str_list: List[str]) -> dict:
            ans = {}
            for i in range(len(str_list)):
                ans[str_list[i]] = i
            return ans
        
        def cal_min_index(dict1: dict, dict2: dict) -> List[str]:
            min_index = len(dict1) + len(dict2)
            ans = []
            for key in dict1.keys():
                if key in dict2:
                    if dict1[key]+dict2[key] < min_index:
                        min_index = dict1[key]+dict2[key]
                        ans = [key]
                    elif dict1[key]+dict2[key] == min_index:
                        ans.append(key)
                    else:
                        pass
            return ans

        dict1 = str_to_dict(list1)
        dict2 = str_to_dict(list2)
        if len(dict1) <= len(dict2):
            return cal_min_index(dict1, dict2)
        else:
            return cal_min_index(dict2, dict1)

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
