class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def cal_pairs(domino_num: int) -> int:
            if domino_num == 1:
                return 0
            else:
                tmp = [i for i in range(1, domino_num)]
                return sum(tmp)

        dominoes_tuple = [tuple(domino) for domino in dominoes]
        domino_dict = {}
        for domino in dominoes_tuple:
            if domino not in domino_dict:
                domino_dict[domino] = 1
            else:
                domino_dict[domino] += 1
        res = 0
        domino_keys = list(domino_dict.keys())
        for domino in domino_keys:
            count = domino_dict[domino]
            res += cal_pairs(domino_dict[domino])
            del domino_dict[domino]
            domino_tmp = list(domino)
            domino_tmp.reverse()
            domino_reverse = tuple(domino_tmp)
            if domino_reverse in domino_dict:
                res += count * domino_dict[domino_reverse]
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
