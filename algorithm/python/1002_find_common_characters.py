class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        def str_to_dict(string: str) -> dict:
            ans_dict = {}
            for ch in string:
                if ch not in ans_dict:
                    ans_dict[ch] = 1
                else:
                    ans_dict[ch] += 1
            return ans_dict

        def cal_common_char_two_dict(dict1: dict, dict2: dict) -> dict:
            ans_dict = {}
            for key in dict1.keys():
                if key in dict2:
                    ans_dict[key] = min(dict1[key], dict2[key])
            return ans_dict

        def dict_to_list(dict1: dict) -> List[str]:
            ans = []
            for key in dict1.keys():
                for i in range(dict1[key]):
                    ans.append(key)
            return ans

        if len(A) == 1:
            return list(A[0])
        else:
            ans_dict = cal_common_char_two_dict(str_to_dict(A[0]), str_to_dict(A[1]))
            for i in range(2, len(A)):
                ans_dict = cal_common_char_two_dict(ans_dict, str_to_dict(A[i]))
            ans = dict_to_list(ans_dict)
            return ans

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
