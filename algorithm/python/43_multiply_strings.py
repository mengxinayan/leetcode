class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiplication_table = {\
        '0': {'0': '00', '1': '00', '2': '00', '3': '00', '4': '00', '5': '00', '6': '00', '7': '00', '8': '00', '9': '00'}, \
        '1': {'0': '00', '1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9': '09'}, \
        '2': {'0': '00', '1': '02', '2': '04', '3': '06', '4': '08', '5': '10', '6': '12', '7': '14', '8': '16', '9': '18'}, \
        '3': {'0': '00', '1': '03', '2': '06', '3': '09', '4': '12', '5': '15', '6': '18', '7': '21', '8': '24', '9': '27'}, \
        '4': {'0': '00', '1': '04', '2': '08', '3': '12', '4': '16', '5': '20', '6': '24', '7': '28', '8': '32', '9': '36'}, \
        '5': {'0': '00', '1': '05', '2': '10', '3': '15', '4': '20', '5': '25', '6': '30', '7': '35', '8': '40', '9': '45'}, \
        '6': {'0': '00', '1': '06', '2': '12', '3': '18', '4': '24', '5': '30', '6': '36', '7': '42', '8': '48', '9': '54'}, \
        '7': {'0': '00', '1': '07', '2': '14', '3': '21', '4': '28', '5': '35', '6': '42', '7': '49', '8': '56', '9': '63'}, \
        '8': {'0': '00', '1': '08', '2': '16', '3': '24', '4': '32', '5': '40', '6': '48', '7': '56', '8': '64', '9': '72'}, \
        '9': {'0': '00', '1': '09', '2': '18', '3': '27', '4': '36', '5': '45', '6': '54', '7': '63', '8': '72', '9': '81'}  }

        addition_table = {\
        '0': {'0': '00', '1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9': '09'}, \
        '1': {'0': '01', '1': '02', '2': '03', '3': '04', '4': '05', '5': '06', '6': '07', '7': '08', '8': '09', '9': '10'}, \
        '2': {'0': '02', '1': '03', '2': '04', '3': '05', '4': '06', '5': '07', '6': '08', '7': '09', '8': '10', '9': '11'}, \
        '3': {'0': '03', '1': '04', '2': '05', '3': '06', '4': '07', '5': '08', '6': '09', '7': '10', '8': '11', '9': '12'}, \
        '4': {'0': '04', '1': '05', '2': '06', '3': '07', '4': '08', '5': '09', '6': '10', '7': '11', '8': '12', '9': '13'}, \
        '5': {'0': '05', '1': '06', '2': '07', '3': '08', '4': '09', '5': '10', '6': '11', '7': '12', '8': '13', '9': '14'}, \
        '6': {'0': '06', '1': '07', '2': '08', '3': '09', '4': '10', '5': '11', '6': '12', '7': '13', '8': '14', '9': '15'}, \
        '7': {'0': '07', '1': '08', '2': '09', '3': '10', '4': '11', '5': '12', '6': '13', '7': '14', '8': '15', '9': '16'}, \
        '8': {'0': '08', '1': '09', '2': '10', '3': '11', '4': '12', '5': '13', '6': '14', '7': '15', '8': '16', '9': '17'}, \
        '9': {'0': '09', '1': '10', '2': '11', '3': '12', '4': '13', '5': '14', '6': '15', '7': '16', '8': '17', '9': '18'}  }

        def multiply_num_one(num1: str, num2: str) -> str:
            # len(num1) >= 1 , len(num2) == 1.
            # num1 = [0-9]*, num2 = [0-9]
            ans = ''
            carry_bit = '0'
            current_bit = ''
            for i in range(len(num1)-1, -1, -1):
                tmp_ans = multiplication_table[num1[i]][num2]
                current_bit = addition_table[tmp_ans[1]][carry_bit]
                if current_bit[0] == '1':
                    carry_bit = addition_table[tmp_ans[0]]['1'][1]
                    #carry_bit = add_one_one(tmp_ans[0], '1')
                else:
                    carry_bit = tmp_ans[0]
                ans = current_bit[1] + ans
            if carry_bit != '0':
                ans = carry_bit + ans
            return ans

        def add_num_num(num1: str, num2: str) -> str:
            # len(num1) <=  len(num2)
            # num1 = [0-9]*, num2 = [0-9]*
            num1 = '0' * (len(num2) - len(num1)) + num1
            ans = ''
            carry_bit = '0'
            for i in range(len(num1)-1, -1, -1):
                num_sum = addition_table[num1[i]][num2[i]]
                add_carry_sum = addition_table[num_sum[1]][carry_bit]
                if (num_sum[0] == '1') or (add_carry_sum[0] == '1'):
                    carry_bit = '1'
                else:
                    carry_bit = '0'
                ans = add_carry_sum[1] + ans
            if carry_bit == '1':
                ans = carry_bit + ans
            return ans

        def multiply_num_num(num1: str, num2: str) -> str:
            # num1 != '0', num2 != '0'
            # num1 = [0-9]*, num2 = [0-9]*
            tmp_sum_arr = []
            ans = '0'
            count = 0
            for i in range(len(num2)-1, -1, -1):
                tmp = multiply_num_one(num1, num2[i]) + count * '0'
                count += 1
                tmp_sum_arr.append(tmp)
            for tmp_sum in tmp_sum_arr:
                ans = add_num_num(ans, tmp_sum)
            return ans

        if (num1 == '0') or (num2 == '0'):
            return '0'
        return multiply_num_num(num1, num2)

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
