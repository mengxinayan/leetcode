class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        def str_to_dict(string: str) -> dict:
            res_dict = {}
            for ch in string:
                if ch not in res_dict:
                    res_dict[ch] = 1
                else:
                    res_dict[ch] += 1
            return res_dict

        def cal_common_char_two_dict(dict1: dict, dict2: dict) -> dict:
            res_dict = {}
            for key in dict1.keys():
                if key in dict2:
                    res_dict[key] = min(dict1[key], dict2[key])
            return res_dict

        def dict_to_list(dict1: dict) -> List[str]:
            res = []
            for key in dict1.keys():
                for i in range(dict1[key]):
                    res.append(key)
            return res

        if len(A) == 1:
            return list(A[0])
        else:
            res_dict = cal_common_char_two_dict(str_to_dict(A[0]), str_to_dict(A[1]))
            for i in range(2, len(A)):
                res_dict = cal_common_char_two_dict(res_dict, str_to_dict(A[i]))
            res = dict_to_list(res_dict)
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
